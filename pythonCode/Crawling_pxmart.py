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
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
    Cache-Control: no-cache
    Connection: keep-alive
    Cookie: JSESSIONID=0000E4wuOYFjU_Ofg5ZbfzN02Ej:-1; _ga=GA1.3.1914857536.1524711838; _gid=GA1.3.1481704526.1524711838; amnetjs_ses=yGJpSAUzB2i3vpRc
    Host: www.pxmart.com.tw
    Pragma: no-cache
    Referer: http://www.pxmart.com.tw/px/map.px
    User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
    X-Requested-With: XMLHttpRequest'''
    headers={i.split(":")[0].strip():i.split(":")[1].strip() for i in headerstr.split("\n")}
    
    paramstr='''id: 420453184803564
    ev: SubscribedButtonClick
    dl: http://www.pxmart.com.tw/px/map.px
    rl: http://www.pxmart.com.tw/px/index.px
    if: false
    ts: 1524711902411
    cd[buttonText]: 搜尋
    cd[buttonFeatures]: {"name":"","id":"btn-search","tag":"a","classList":"paxmart-map-search-btn","innerText":"搜尋","numChildButtons":0,"destination":"javascript:void(0)"}
    cd[formFeatures]: []
    sw: 1600
    sh: 900
    v: 2.8.14
    r: stable
    ec: 4
    o: 28
    it: 1524711876032
    es: automatic'''
    params={i.split(":")[0].strip():i.split(":")[1].strip() for i in paramstr.split("\n")}
    url='''http://www.pxmart.com.tw/px/store1?cityid=&cityzoneid=&cityroadid=&name_short='''
    res=requests.get(url,params=params,headers=headers)
    
    
    
    pxmartDatasO=json.loads(res.text)
    pxmartDatas=[]
    for i in pxmartDatasO:
        pxmartData={}
        pxmartData['name']="全聯"+i['name_short']
        pxmartData['lat']=i['mapy']
        pxmartData['lng']=i['mapx']
        if ")" in i['address']:
            pxmartData['address']=i['address'].split(")")[1] 
        else:
            pxmartData['address']=i['address']
        pxmartData['bigadd']=i['city']
        pxmartData['smalladd']=i['cityzone']
        pxmartData['road']=i['cityroad']
        pxmartData['tele']=i['tel_zno']+"-"+i['tel_no']
        pxmartData['_id']=pxmartData['name']
        pxmartDatas.append(pxmartData)
    Client=pymongo.MongoClient('localhost',27017,username='j122085',password='850605')
    collection=Client.rawData.pxmart
    ids=[i.pop("_id") for i in pxmartDatas]
    writeList=[UpdateOne({"_id":idn},{"$set":data},upsert=True) for idn,data in zip(ids,pxmartDatas)]
    try:
        collection.bulk_write(writeList,ordered=False)
    except Exception as er:
        print(er)

    mailTo("CrawlerPxmart",["andy.yuan@wowprime.com"],"finish")
except Exception as er:
    mailTo("CrawlerPxmart",["andy.yuan@wowprime.com"],"loss error:"+str(er))
