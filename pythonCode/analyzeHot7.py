import json
import pymongo
from pymongo import UpdateOne
import numpy
import math
from math import radians, cos, sin, asin, sqrt
from collections import Counter
import time
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
import smtplib
import gc
gc.enable() 



def haversine(lng1, lat1, lng2, lat2):
    # 将十进制度数转化为弧度
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])
    # haversine公式
    dlng = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlng / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000


b=time.time()
def mailTo(title,mailAdds,message,whoSend='taiwanInfoHot7'):
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

mailTo(title="taiwanInfoHot7begin",mailAdds=["andy.yuan@wowprime.com"],message="分析開始")
try:
    ######################################################第一次跑用stoneTwo來篩選沒超商的點
    b=time.time()
    client = pymongo.mongo_client.MongoClient("localhost", 27017, username='j122085', password='850605')
#     collectionTaiwan = client.rawData.taiwanInfoStoneTwo
    collectionTaiwan = client.rawData.taiwanInfoHot7
    ##################################################第一次跑不執行
    TWLocs=list(collectionTaiwan.find({}, {'_id': False}))
    ##################################################第一次跑不執行
    
    ######################################################IPEEN
    # collection = client.rawData.wowprimeipeen
    collection = client.rawData.ipeenInfo
    ipeendata = list(collection.find({}, {'_id': False}))
    ipeendata = [dien for dien in ipeendata if dien['status'] == "正常營業"
                 and dien['lat'] > 18
                 and dien['lat'] < 27
                 and dien['lng'] < 125
                 and dien['lng'] > 117
                 and dien['bigadd'] != 0
                 and dien['smalladd'] != 0
                 and dien['averagecost'] < 250]

    ######################################################IPEEN
    ######################################################conStore0320
    collection = client.rawData.conStore
    conStoreData = list(collection.find({}, {'_id': False}))
    ######################################################conStore0320
    ######################################################Watsons
    collection = client.rawData.Watsons
    watsonsData = list(collection.find({}, {'_id': False}))
    ######################################################Watsons
    ######################################################carrefour0504
    collection = client.rawData.carrefour
    carrefourData = list(collection.find({}, {'_id': False}))
    ######################################################carrefour0504
    ######################################################pxmart0504
    collection = client.rawData.pxmart
    pxmartData = list(collection.find({}, {'_id': False}))
    ######################################################pxmart0504
    ######################################################Clinic0531
    collection = client.rawData.infoClinic
    clinicData = list(collection.find({}, {'_id': False}))
    ######################################################Clinic0531
    ######################################################Tstore0531
    collection = client.rawData.info3Store
    tStoreData = list(collection.find({}, {'_id': False}))
    ######################################################Tstore0531
    ##################################################第一次跑先去除latlng以外的資訊
#     TWLocs = [{"lat":i["lat"],"lng":i["lng"]} for i in TWLocs if ('NconStore_Analyze' in i and
#               i['NconStore_Analyze'] >0)]
    TWLocs = [i for i in TWLocs if ('NconStore_Analyze' in i and
              i['NconStore_Analyze'] >0)]
    ##################################################第一次跑先去除latlng以外的資訊
    allN=len(TWLocs)
    print("有{}筆資料要分析".format(allN))
    radius=500
    n = 0

    for TWLoc in TWLocs:
        score=0
        n += 1
        if n % 50 == 0:
            e=time.time()
            print("已完成{}%分析-{}項,花費{}秒".format(round(n/allN,4)*100,n,round(e-b)))
        if n % 2000 == 0:
            gc.collect()
            client = pymongo.mongo_client.MongoClient("localhost", 27017, username='j122085', password='850605')
            collection = client.rawData.taiwanInfoHot7
            
            ids=["{}_{}".format(i['lat'],i['lng']) for i in TWLocs if i.get("NconStore_Analyze",0)>0]
            datas=[i for i in TWLocs if i.get("NconStore_Analyze",0)>0]
            operations=[UpdateOne({"_id":idn},{'$set':data},upsert=True) for idn ,data in zip(ids,datas)]
            try:
                collection.bulk_write(operations ,ordered=False)
            except Exception as er:
                print(er)
            client.close()

        TWLoc["areaRadius_Analyze"] = radius
        #############################################################0523Score

        TWLoc["NconStore_Analyze"] = len([dien['name'] for dien in conStoreData if "lng" in dien and haversine(lng1=float(dien["lng"]),
                                                                                lat1=float(dien["lat"]),
                                                                                lng2=TWLoc["lng"],
                                                                                lat2=TWLoc["lat"]) <= radius])
            
        
        TWLoc["Nwatson_Analyze"] = len([dien for dien in watsonsData
                                          if haversine(lng1=float(dien["lng"]),
                                                       lat1=float(dien["lat"]),
                                                       lng2=TWLoc["lng"],
                                                       lat2=TWLoc["lat"]) <= radius])
        TWLoc["Npxmart_Analyze"] = len([dien for dien in pxmartData
                                          if haversine(lng1=float(dien["lng"]),
                                                       lat1=float(dien["lat"]),
                                                       lng2=TWLoc["lng"],
                                                       lat2=TWLoc["lat"]) <= radius])
        
            
        TWLoc["NclinicData_Analyze"] = len([dien for dien in clinicData
                                  if haversine(lng1=float(dien["lng"]),
                                               lat1=float(dien["lat"]),
                                               lng2=TWLoc["lng"],
                                               lat2=TWLoc["lat"]) <= radius])
        
        TWLoc["NtStore_Analyze"] = len([dien for dien in tStoreData
                                  if haversine(lng1=float(dien["lng"]),
                                               lat1=float(dien["lat"]),
                                               lng2=TWLoc["lng"],
                                               lat2=TWLoc["lat"]) <= radius])

        rangeCost = 1.4

        simDien = [dien['smallstyle'] for dien in ipeendata if haversine(lng1=dien["lng"],
                                                                       lat1=dien["lat"],
                                                                       lng2=TWLoc["lng"],
                                                                       lat2=TWLoc["lat"]) <= 500
                   and dien['averagecost'] < 250
                   and dien['smallstyle']=="鐵板燒"]
        
        TWLoc["NsimCostDien"] = len(simDien)

        dapu = len([dien['smallstyle'] for dien in ipeendata if haversine(lng1=dien["lng"],
                                                                       lat1=dien["lat"],
                                                                       lng2=TWLoc["lng"],
                                                                       lat2=TWLoc["lat"]) <= 500
                   and "大埔平" in dien['name']])
        
        TWLoc["NDapu_analyze"] = dapu
        

        

        #############################################################0523Score
    for i in TWLocs:
        score=0
        if i['NclinicData_Analyze']>20:
            score+=2
        elif i['NclinicData_Analyze']>9:
            score+=1
        if i['NconStore_Analyze']>11:
            score+=2
        elif i['NconStore_Analyze']>5:
            score+=1
        if i['Npxmart_Analyze']+i['Nwatson_Analyze']>2:
            score+=2
        elif i['Npxmart_Analyze']+i['Nwatson_Analyze']>0:
            score+=1

        if i['NsimCostDien']>3:
            score+=3
        elif i['NsimCostDien']>2:
            score+=2
        elif i['NsimCostDien']>1:
            score+=1
        if i['NtStore_Analyze']+i["NDapu_analyze"]>0:
            score+=1
        i['score']=score
        
    
    e = time.time()
    print(e-b)


#     client.close()
    client = pymongo.mongo_client.MongoClient("localhost", 27017, username='j122085', password='850605')
    collection = client.rawData.taiwanInfoHot7
    ids=["{}_{}".format(i['lat'],i['lng']) for i in TWLocs]
    operations=[UpdateOne({"_id":idn},{'$set':data},upsert=True) for idn ,data in zip(ids,TWLocs)]
    try:
        collection.bulk_write(operations ,ordered=False)
    except Exception as er:
        print(er)
    client.close()
    
    e = time.time()
    print(e-b)
    
    
    mailTo(title="taiwanInfoHot7Success",mailAdds=["andy.yuan@wowprime.com"],message="分析完畢_耗時{}秒".format(e-b))
except Exception as er:
    errorMsg=str(er)+"出錯位置:"+str(sys.exc_info()[2].tb_lineno)
    mailTo(title="taiwanInfoHot7Fail",mailAdds=["andy.yuan@wowprime.com"],message=errorMsg)
