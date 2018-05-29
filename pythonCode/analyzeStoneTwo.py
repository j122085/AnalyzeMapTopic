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
def mailTo(title,mailAdds,message,whoSend='AutoAddInsurance'):
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
    ######################################################IPEEN
    b=time.time()
    queryElements = {}
    client = pymongo.mongo_client.MongoClient("localhost", 27017, username='j122085', password='850605')
    collectionTaiwan = client.rawData.taiwanInfoStoneTwo
    ##################################################第一次跑不執行
    TWLocs=list(collectionTaiwan.find({}, {'_id': False}))
    ##################################################第一次跑不執行
    
    
    # collection = client.rawData.wowprimeipeen
    collection = client.rawData.ipeenInfo
    ipeendata = list(collection.find(queryElements))
    ipeendata = [dien for dien in ipeendata if dien['status'] == "正常營業"
                 and dien['lat'] > 18
                 and dien['lat'] < 27
                 and dien['lng'] < 125
                 and dien['lng'] > 117
                 and dien['bigadd'] != 0
                 and dien['smalladd'] != 0
                 and dien['averagecost'] < 8000]

    for dien in ipeendata:
        dien["id"] = dien.pop("_id")
    ######################################################IPEEN
    ######################################################104
    collection = client.rawData.HRdata104
    hr104data = list(collection.find(queryElements))
    hr104data = [dien for dien in hr104data if dien['LAT'] > 18
                 and dien['LAT'] < 27
                 and dien['SAL_MONTH_LOW'] > 18000
                 and dien['SAL_MONTH_LOW'] < 100000
                 and dien['SAL_MONTH_HIGH'] > 18000
                 and dien['SAL_MONTH_HIGH'] < 200000
                 and dien['LON'] < 125
                 and dien['LON'] > 117
                 and dien['bigadd'] != 0
                 and dien['smalladd'] != 0]

    for dien in hr104data:
        dien["lat"] = dien.pop("LAT")
        dien["lng"] = dien.pop("LON")
        del dien["_id"]
    ######################################################104
    ######################################################Nhuman
    collection = client.rawData.Nhuman
    Nhumandata = list(collection.find(queryElements))
    for dien in Nhumandata:
        dien["weight"] = int(dien.pop("Nhuman"))
        dien["add"] = dien.pop("_id")
    ######################################################Nhuman
    ######################################################CostPower
    collection = client.rawData.CostPower
    CostPowerdata = list(collection.find(queryElements))
    for dien in CostPowerdata:
        dien["weight"] = int(dien.pop('costPower'))
        dien["add"] = dien.pop("_id")
    ######################################################CostPower
    ######################################################Bus0320
    collection = client.rawData.busData
    busData = list(collection.find(queryElements))
    for dien in busData:
        dien["add"] = dien.pop("_id")
    ######################################################Bus0320
    ######################################################conStore0320
    collection = client.rawData.conStore
    conStoreData = list(collection.find(queryElements))
    for dien in conStoreData:
        dien.pop("_id")
    ######################################################conStore0320
    ######################################################Watsons
    collection = client.rawData.Watsons
    watsonsData = list(collection.find(queryElements))
    for dien in watsonsData:
        dien.pop("_id")
    ######################################################Watsons
    ######################################################carrefour0504
    collection = client.rawData.carrefour
    carrefourData = list(collection.find(queryElements))
    for dien in carrefourData:
        dien.pop("_id")
    ######################################################carrefour0504
    ######################################################pxmart0504
    collection = client.rawData.pxmart
    pxmartData = list(collection.find(queryElements))
    for dien in pxmartData:
        dien.pop("_id")
    ######################################################pxmart0504
    ######################################################Wow
    ##################################################第一次跑不執行
    TWLocs = [i for i in TWLocs if ('NconStore_Analyze' in i and
              i['NconStore_Analyze'] >0)]
    ##################################################第一次跑不執行
    allN=len(TWLocs)
    print("有{}筆資料要分析".format(allN))
    radius=500
    n = 0
    
    
    for TWLoc in TWLocs:
        score=0
        
        n += 1
        if n % 100 == 0:
            e=time.time()
            print("已完成{}%分析-{}項,花費{}秒".format(round(n/allN,4)*100,n,round(e-b)))
        if n % 2000 == 0:
            gc.collect()
            client = pymongo.mongo_client.MongoClient("localhost", 27017, username='j122085', password='850605')
            collection = client.rawData.taiwanInfoStoneTwo
            
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
        if TWLoc["NconStore_Analyze"]>12:
            score=score+2
        elif TWLoc["NconStore_Analyze"]>4:
            score=score+1
            
        if TWLoc["NconStore_Analyze"]==0:
            TWLoc["score"]=score
            continue
            
            
        TWLoc["NbusStation_Analyze"] = len([dien['stationName'] for dien in busData if "lng" in dien and haversine(lng1=dien["lng"],
                                                                                lat1=dien["lat"],
                                                                                lng2=TWLoc["lng"],
                                                                                lat2=TWLoc["lat"]) <= 500])#0326 change radius
        if TWLoc["NbusStation_Analyze"]>11:
            score=score+2
        elif TWLoc["NbusStation_Analyze"]>4:
            score=score+1
        
        
    #         conStoreData
        TWLoc["Nstar_Analyze"] = len([dien['name'] for dien in ipeendata 
                                if '星巴' in dien['name'] 
                                and haversine(lng1=dien["lng"],
                                              lat1=dien["lat"],
                                              lng2=TWLoc["lng"],
                                              lat2=TWLoc["lat"]) <= radius])
        TWLoc["Nmc_Analyze"] = len([dien['name'] for dien in ipeendata 
                                if '麥當' in dien['name'] 
                                and haversine(lng1=dien["lng"],
                                              lat1=dien["lat"],
                                              lng2=TWLoc["lng"],
                                              lat2=TWLoc["lat"]) <= radius])
        TWLoc["Nken_Analyze"] = len([dien['name'] for dien in ipeendata 
                                if '肯德' in dien['name'] 
                                and haversine(lng1=dien["lng"],
                                              lat1=dien["lat"],
                                              lng2=TWLoc["lng"],
                                              lat2=TWLoc["lat"]) <= radius])
        TWLoc["Nwa_Analyze"] = len([dien['name'] for dien in ipeendata 
                                if '瓦城泰' in dien['name'] 
                                and haversine(lng1=dien["lng"],
                                              lat1=dien["lat"],
                                              lng2=TWLoc["lng"],
                                              lat2=TWLoc["lat"]) <= radius])
        
        if TWLoc["Nstar_Analyze"]+TWLoc["Nmc_Analyze"]+TWLoc["Nken_Analyze"]+TWLoc["Nwa_Analyze"]>2:
            score=score+2
        elif TWLoc["Nstar_Analyze"]+TWLoc["Nmc_Analyze"]+TWLoc["Nken_Analyze"]+TWLoc["Nwa_Analyze"]>0:
            score=score+1
        
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
        
        if TWLoc["Nwatson_Analyze"]+TWLoc["Npxmart_Analyze"]>2:
            score=score+2
        elif TWLoc["Nwatson_Analyze"]+TWLoc["Npxmart_Analyze"]>0:
            score=score+1
            
        
        
        
        
        rangeCost = 1.4

        simDien = [dien['bigstyle'] for dien in ipeendata if haversine(lng1=dien["lng"],
                                                                       lat1=dien["lat"],
                                                                       lng2=TWLoc["lng"],
                                                                       lat2=TWLoc["lat"]) <= 500
                   and dien['averagecost'] < ((240) * rangeCost)
                   and dien['averagecost'] > ((240) / rangeCost)]
        # stoneTwoCost==240
        TWLoc["NsimCostDien"] = len(simDien)
        # print(simDien)
        # print(wowDien['Called'])
        if TWLoc["NsimCostDien"]>29:
            score=score+2
        elif TWLoc["NsimCostDien"]>11:
            score=score+1
        
        
        
            
            
        TWLoc["score"]=score
        
        dienHuman = sum([dien['weight'] for dien in Nhumandata if haversine(lng1=dien["lng"],
                                                                            lat1=dien["lat"],
                                                                            lng2=TWLoc["lng"],
                                                                            lat2=TWLoc["lat"]) <= radius and 'weight' in dien])
        TWLoc['Nhuman_Analyze'] = dienHuman

        #############################################################0523Score
        
        
        
    e = time.time()
    print(e-b)


#     ids=[data.pop("_id") for data in TWLocs]
#     operations=[UpdateOne({"_id":idn},{'$set':data},upsert=True) for idn ,data in zip(ids,TWLocs)]
#     try:
#         collection.bulk_write(operations ,ordered=False)
#     except Exception as er:
#         print(er)

#     alldata=list(collection.find({}))

#     client.close()
    client = pymongo.mongo_client.MongoClient("localhost", 27017, username='j122085', password='850605')
    collection = client.rawData.taiwanInfoStoneTwo
    ids=["{}_{}".format(i['lat'],i['lng']) for i in TWLocs]
    operations=[UpdateOne({"_id":idn},{'$set':data},upsert=True) for idn ,data in zip(ids,TWLocs)]
    try:
        collection.bulk_write(operations ,ordered=False)
    except Exception as er:
        print(er)
    client.close()
    
    e = time.time()
    print(e-b)
    
    
    mailTo(title="TaiwanDataSuccess",mailAdds=["andy.yuan@wowprime.com"],message="分析完畢_耗時{}秒".format(e-b),whoSend='analyzeTaiwanData')
except Exception as er:
    errorMsg=str(er)+"出錯位置:"+str(sys.exc_info()[2].tb_lineno)
    mailTo(title="analyzeTaiwanDataFail",mailAdds=["andy.yuan@wowprime.com"],message=errorMsg,whoSend='analyzeTaiwanData')
