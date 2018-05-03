import requests
import pymongo
from pymongo import UpdateOne
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
import smtplib
import json

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



try:
    headerstr='''Accept: application/json, text/javascript, */*; q=0.01
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
    Cache-Control: no-cache
    Connection: keep-alive
    Cookie: _ga=GA1.3.207086480.1524637160; _gid=GA1.3.1652140068.1524637160
    Host: www.carrefour.com.tw
    Pragma: no-cache
    Referer: https://www.carrefour.com.tw/store.html
    User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
    X-Requested-With: XMLHttpRequest'''

    headers={i.split(":")[0].strip():i.split(":")[1].strip() for i in headerstr.split("\n")}
    res=requests.get("https://www.carrefour.com.tw/api/Store",headers=headers)
    carrefourDatasO=json.loads(res.text)['result']
    carrefourDatas=[]
    for i in carrefourDatasO:
        carrefourData={}
        carrefourData['name']="家樂福"+i['分店中文名稱']
        carrefourData['lat']=i['Latitude']
        carrefourData['lng']=i['Longitude']
        carrefourData['address']=i['地址']
        carrefourData['bigadd']=i['縣市']
        carrefourData['smalladd']=i['區']
        carrefourData['tele']=i['電話號碼']
        carrefourData['_id']=carrefourData['name']
        carrefourDatas.append(carrefourData)
    Client=pymongo.MongoClient('localhost',27017,username='j122085',password='850605')
    collection=Client.rawData.carrefour
    ids=[i.pop("_id") for i in carrefourDatas]
    writeList=[UpdateOne({"_id":idn},{"$set":data},upsert=True) for idn,data in zip(ids,carrefourDatas)]
    try:
        collection.bulk_write(writeList,ordered=False)
    except Exception as er:
        print(er)

    mailTo("CrawlerCarrefour",["andy.yuan@wowprime.com"],"finish")
except Exception as er:
    mailTo("CrawlerCarrefour",["andy.yuan@wowprime.com"],"loss error:"+str(er))
