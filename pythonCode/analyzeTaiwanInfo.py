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
    collectionTaiwan = client.rawData.taiwanInfo
    TWLocs=list(collectionTaiwan.find({}))
    
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
    ######################################################Wow


    TWLocs = [i for i in TWLocs if ('costPower_Analyze' in i and
              i['costPower_Analyze'] >0) or
              ('Nhuman_Analyze' in i and
              i['Nhuman_Analyze']>0)]
    allN=len(TWLocs)
    print("有{}筆資料要分析".format(allN))
    radius=2000
    n = 0
    for TWLoc in TWLocs:
        n += 1
        if n % 15 == 0:
            print("已完成{}%分析-{}項".format(round(n/allN,4)*100,n))
        if n % 1000 == 0:
            for i in TWLocs:
                i["_id"]="{}_{}".format(i['lat'],i['lng'])
            client = pymongo.mongo_client.MongoClient("localhost", 27017, username='j122085', password='850605')
            collection = client.rawData.taiwanInfo
            ids=[data.pop("_id") for data in TWLocs]
            operations=[UpdateOne({"_id":idn},{'$set':data},upsert=True) for idn ,data in zip(ids,TWLocs)]
            try:
                collection.bulk_write(operations ,ordered=False)
            except Exception as er:
                print(er)
            client.close()

        TWLoc["areaRadius_Analyze"] = radius
        dienCostPower = round(numpy.mean([dien['weight'] for dien in CostPowerdata if haversine(lng1=dien["lng"],
                                                                                                lat1=dien["lat"],
                                                                                                lng2=TWLoc["lng"],
                                                                                                lat2=TWLoc[
                                                                                                    "lat"]) <= radius and 'weight' in dien]))

        if not math.isnan(dienCostPower):
            TWLoc["costPower_Analyze"] = dienCostPower
        else:
            TWLoc["costPower_Analyze"] =0
        TWLoc["NcostData_Analyze"] = len([dien['weight'] for dien in CostPowerdata if haversine(lng1=dien["lng"],
                                                                                lat1=dien["lat"],
                                                                                lng2=TWLoc["lng"],
                                                                                lat2=TWLoc["lat"]) <= radius and 'weight' in dien])

        dienHuman = sum([dien['weight'] for dien in Nhumandata if haversine(lng1=dien["lng"],
                                                                            lat1=dien["lat"],
                                                                            lng2=TWLoc["lng"],
                                                                            lat2=TWLoc["lat"]) <= radius and 'weight' in dien])
        TWLoc['Nhuman_Analyze'] = dienHuman

        avgSalary = round(numpy.mean(
            [dien['SAL_MONTH_LOW'] * 1 / 3 + dien['SAL_MONTH_HIGH'] * 2 / 3 for dien in hr104data if
             haversine(lng1=dien["lng"],
                       lat1=dien["lat"],
                       lng2=TWLoc["lng"],
                       lat2=TWLoc["lat"]) <= radius and 'SAL_MONTH_HIGH' in dien and 'SAL_MONTH_LOW' in dien]))
        if not math.isnan(avgSalary):
            TWLoc['avgSalary_Analyze'] = avgSalary
        else:
            TWLoc["avgSalary_Analyze"] =0

        TWLoc['Njob_Analyze'] = len([dien['SAL_MONTH_LOW'] * 1 / 3 + dien['SAL_MONTH_HIGH'] * 2 / 3 for dien in hr104data if
                            haversine(lng1=dien["lng"],
                                      lat1=dien["lat"],
                                      lng2=TWLoc["lng"],
                                      lat2=TWLoc["lat"]) <= radius and 'SAL_MONTH_HIGH' in dien  and 'SAL_MONTH_LOW' in dien])

        avgCost = round(numpy.mean([dien['averagecost'] for dien in ipeendata if haversine(lng1=dien["lng"],
                                                                                           lat1=dien["lat"],
                                                                                           lng2=TWLoc["lng"],
                                                                                           lat2=TWLoc[
                                                                                               "lat"]) <= radius and 'averagecost' in dien]))
        if not math.isnan(avgCost):
            TWLoc['avgCost_Analyze'] = avgCost
        else:
            TWLoc["avgCost_Analyze"] =0

        try:
            mostStyle = Counter([dien['bigstyle'] for dien in ipeendata if haversine(lng1=dien["lng"],
                                                                                     lat1=dien["lat"],
                                                                                     lng2=TWLoc["lng"],
                                                                                     lat2=TWLoc[
                                                                                         "lat"]) <= radius and 'bigstyle' in dien]).most_common(1)[0][0]
        except:
            mostStyle = ""
        TWLoc['mostStyle_Analyze'] = mostStyle

        ###############################################################################################################0320
        TWLoc["NbusStation_Analyze"] = len([dien['stationName'] for dien in busData if "lng" in dien and haversine(lng1=dien["lng"],
                                                                                lat1=dien["lat"],
                                                                                lng2=TWLoc["lng"],
                                                                                lat2=TWLoc["lat"]) <= 500])#0326 change radius

        TWLoc["NconStore_Analyze"] = len([dien['name'] for dien in conStoreData if "lng" in dien and haversine(lng1=float(dien["lng"]),
                                                                                lat1=float(dien["lat"]),
                                                                                lng2=TWLoc["lng"],
                                                                                lat2=TWLoc["lat"]) <= radius])
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
        ################################################################################################################0320
        
        
        
        
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
    for i in TWLocs:
        i["_id"]="{}_{}".format(i['lat'],i['lng'])
    client = pymongo.mongo_client.MongoClient("192.168.1.113", 27017, username='j122085', password='850605')
    collection = client.rawData.taiwanInfo
    ids=[data.pop("_id") for data in TWLocs]
    operations=[UpdateOne({"_id":idn},{'$set':data},upsert=True) for idn ,data in zip(ids,TWLocs)]
    try:
        collection.bulk_write(operations ,ordered=False)
    except Exception as er:
        print(er)
    client.close()
    
    mailTo(title="TaiwanDataSuccess",mailAdds=["andy.yuan@wowprime.com"],message="分析完畢_耗時{}秒".format(e-b),whoSend='analyzeTaiwanData')
except Exception as er:
    errorMsg=str(er)+"出錯位置:"+str(sys.exc_info()[2].tb_lineno)
    mailTo(title="analyzeTaiwanDataFail",mailAdds=["andy.yuan@wowprime.com"],message=errorMsg,whoSend='analyzeTaiwanData')
