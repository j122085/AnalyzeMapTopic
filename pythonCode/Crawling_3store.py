import requests
from bs4 import BeautifulSoup as bs
import sys
import time
import json
import pymongo
from pymongo import UpdateOne
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
import smtplib

def mailTo(title,mailAdds,message,whoSend='CrawlerThreeStore'):
    msg = MIMEMultipart()    
    sender = whoSend
    subject = title
    body = message
    msg['From'] = sender
    msg['To'] = ','.join(mailAdds)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    text=msg.as_string()
    #print text
    # Send the message via our SMTP server
    s = smtplib.SMTP('192.168.2.1',25)
    s.sendmail(sender,mailAdds, text)
    s.quit()  

mailTo("CrawlerThreeStoreBegin",["andy.yuan@wowprime.com"],"go")

headerStrs="""Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
Connection: keep-alive
Content-Length: 80
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: _ga=GA1.3.1829003529.1527650814; _gid=GA1.3.2024599854.1527650814; _gat=1
Host: www.3375.com.tw
Origin: http://www.3375.com.tw
Referer: http://www.3375.com.tw/Stores/StoresInfo
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36
X-Requested-With: XMLHttpRequest"""
headerDict={i.split(":")[0]:i.split(":")[1].strip() for i in headerStrs.split("\n")}



dataStrs="""QueryStoreArea: 
QueryCity: 
city: 
QueryStoreClass: 
page: 1
sortCol: 
sortDesc: false"""
dataDict={i.split(":")[0]:i.split(":")[1].strip() for i in dataStrs.split("\n")}


res=requests.post("http://www.3375.com.tw/Stores/StoresInfo",data=dataDict,headers=headerDict)
soup=bs(res.text,"lxml")
threeStorelist=[k for j in  ["\n".join(i.split("\n\n\n")[:-2]).replace("\t","").split("\n") for i in soup.text.split("\n\n\n\n")[1:]] for k in j]

dienList=[]
for i in range(len(threeStorelist[:-3])//5+1):
    dien={}
    data=threeStorelist[i*5:i*5+5]
    dien['name']=data[0]
    dien['tel']=data[1]
    dien['address']=data[2]
    ###############
    try:
        dien["bigadd"] = re.findall("(\w\w[市|縣])(\w\w?\w?[區|市|鎮|鄉])", dien['address'])[0][0]
        dien["smalladd"] = re.findall("(\w\w[市|縣])(\w\w?\w?[區|市|鎮|鄉])", dien['address'])[0][1]
    except:
        dien["bigadd"] = 0
        dien["smalladd"] = 0
    ##############
    try:
        dien['type']=data[3]
        dien['open']=data[4]
    except:
        pass
    dienList.append(dien)





try:
    nn=0
    Alln=len(dienList)
    for dien in dienList:
        address=dien['address'].split(".")[0].split("、")[0].split("號")[0]
        nn+=1
        if nn%30==0:
            print("{}%".format(round(nn/Alln,2)*100))
        if 'lat' not in dien or dien['lat']=='24.1491968':
            add='沒有地址'
            n=0
            while add=='沒有地址':
                res=requests.get('http://3wa.tw/API/getTGOSAddress_XY?address='+address)
                add=res.text
                n+=1
                time.sleep(0.4)
                if n >10:
                    break
            try:
                jsonData=json.loads(add)
                dien['lat']=jsonData['lat']
                dien['lng']=jsonData['long']
                print(address,dien['lat'],dien['lng'])
            except:
                print(address+"轉換失敗")

    # 用googleApi轉換
    import googlemaps
    gmaps = googlemaps.Client(key='AIzaSyAF9GKxqgmgDEW_h7M4TtM5CbkK03xnS0E')
    for dien in dienList:
        address=dien['address'].split(".")[0].split("、")[0].split("號")[0]
        try:
            if 'lat' not in dien or dien['lat']=='24.1491968':
                #關閉的店、店號有A的、大陸的店都不需要做
                    geocode_result = gmaps.geocode(address)
                    if geocode_result==[]:
                        geocode_result = gmaps.geocode(address[:11])            
                    dien['lat']=geocode_result[0]['geometry']['location']['lat']
                    dien['lng']=geocode_result[0]['geometry']['location']['lng']
                    print(address,dien['lat'],dien['lng'])
                    time.sleep(1.5)

        except Exception as e:
            print(e)
            print(address+"無經緯度資料")


            
    client=pymongo.MongoClient('localhost',27017,username='j122085',password='850605')
    collection=client.rawData.info3Store
    
    ids=[data["name"] for data in dienList]
    operations=[UpdateOne({"_id":idn},{'$set':data},upsert=True) for idn ,data in zip(ids,dienList)]
    try:
        collection.bulk_write(operations ,ordered=False)
    except Exception as er:
        print(er)
        
    mailTo("CrawlerThreeStoreSuccess",["andy.yuan@wowprime.com"],"轉換地址完畢 共{}筆".format(Alln))
except Exception as er:
    errorstr="出錯"+str(er)+"出錯位置:"+str(sys.exc_info()[2].tb_lineno)
    mailTo("CrawlerThreeStoreError",["andy.yuan@wowprime.com"],"轉換地址失敗"+errorstr)

