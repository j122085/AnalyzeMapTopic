import requests
import time
import pymongo
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
import smtplib
import sys

def mailTo(title,mailAdds,message,whoSend='Crawler591Info'):
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

mailTo("trans591LatLngBegin",["andy.yuan@wowprime.com"],"go")


client=pymongo.MongoClient('localhost',27017,username='j122085',password='850605')
collection=client.rawData.info591
data591s=list(collection.find({}))



try:
    nn=0
    Alln=len(data591s)
    for dien in data591s:
        address = dien['address'].split(".")[0].split("、")[0].split("號")[0]
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
    for dien in data591s:
        address = dien['address'].split(".")[0].split("、")[0].split("號")[0]
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


    from pymongo import UpdateOne
    [i.pop('_id', None) for i in data591s]
    ids=[data["url"].split("-")[-1].split(".")[0] for data in data591s]
    operations=[UpdateOne({"_id":idn},{'$set':data},upsert=True) for idn ,data in zip(ids,data591s)]
    try:
        collection.bulk_write(operations ,ordered=False)
    except Exception as er:
        print(er)
        
    mailTo("trans591LatLngSuccess",["andy.yuan@wowprime.com"],"轉換地址完畢 共{}筆".format(Alln))
except Exception as er:
    errorstr="出錯"+str(er)+"出錯位置:"+str(sys.exc_info()[2].tb_lineno)
    mailTo("trans591LatLngError",["andy.yuan@wowprime.com"],"轉換地址失敗"+errorstr)
