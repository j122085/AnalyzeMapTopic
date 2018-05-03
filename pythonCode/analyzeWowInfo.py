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
    collection = client.rawData.wowprimediendata
    wowDiensData = list(collection.find({'CloseDate': 'None', "lat": {"$gt": 1}}))
    wowDiensData = [dien for dien in wowDiensData if "A" not in dien['StoreNo'] and dien['StoreNo'][0] != '3']
    ######################################################Wow
    ######################################################Watsons
    collection = client.rawData.Watsons
    watsonsData = list(collection.find(queryElements))
    for dien in watsonsData:
        dien.pop("_id")
    ######################################################Watsons
    x = []
    queryDien = ""#input("請輸入品牌名稱:")
    radius = 2000#int(input("半徑範圍(公尺):"))
    if queryDien != "":
        wowDiensData = [i for i in wowDiensData if i['Called'] == queryDien]
    else:
        queryDien = "全品牌"
    print("有{}筆資料要分析".format(len(wowDiensData)))
    n = 0
    for wowDien in wowDiensData:
        n += 1
        if n % 15 == 0:
            print("已完成{}項分析".format(n))
        wowDien["areaRadius_Analyze"] = radius
        dienCostPower = round(numpy.mean([dien['weight'] for dien in CostPowerdata if haversine(lng1=dien["lng"],
                                                                                                lat1=dien["lat"],
                                                                                                lng2=wowDien["lng"],
                                                                                                lat2=wowDien[
                                                                                                    "lat"]) <= radius and 'weight' in dien]))

        if not math.isnan(dienCostPower):
            wowDien["costPower_Analyze"] = dienCostPower
        wowDien["NcostData_Analyze"] = len([dien['weight'] for dien in CostPowerdata if haversine(lng1=dien["lng"],
                                                                                lat1=dien["lat"],
                                                                                lng2=wowDien["lng"],
                                                                                lat2=wowDien["lat"]) <= radius and 'weight' in dien])

        dienHuman = sum([dien['weight'] for dien in Nhumandata if haversine(lng1=dien["lng"],
                                                                            lat1=dien["lat"],
                                                                            lng2=wowDien["lng"],
                                                                            lat2=wowDien["lat"]) <= radius and 'weight' in dien])
        wowDien['Nhuman_Analyze'] = dienHuman

        avgSalary = round(numpy.mean(
            [dien['SAL_MONTH_LOW'] * 1 / 3 + dien['SAL_MONTH_HIGH'] * 2 / 3 for dien in hr104data if
             haversine(lng1=dien["lng"],
                       lat1=dien["lat"],
                       lng2=wowDien["lng"],
                       lat2=wowDien["lat"]) <= radius and 'SAL_MONTH_HIGH' in dien and 'SAL_MONTH_LOW' in dien]))
        if not math.isnan(avgSalary):
            wowDien['avgSalary_Analyze'] = avgSalary

        wowDien['Njob_Analyze'] = len([dien['SAL_MONTH_LOW'] * 1 / 3 + dien['SAL_MONTH_HIGH'] * 2 / 3 for dien in hr104data if
                            haversine(lng1=dien["lng"],
                                      lat1=dien["lat"],
                                      lng2=wowDien["lng"],
                                      lat2=wowDien["lat"]) <= radius and 'SAL_MONTH_HIGH' in dien  and 'SAL_MONTH_LOW' in dien])

        avgCost = round(numpy.mean([dien['averagecost'] for dien in ipeendata if haversine(lng1=dien["lng"],
                                                                                           lat1=dien["lat"],
                                                                                           lng2=wowDien["lng"],
                                                                                           lat2=wowDien[
                                                                                               "lat"]) <= radius and 'averagecost' in dien]))
        if not math.isnan(avgCost):
            wowDien['avgCost_Analyze'] = avgCost

        try:
            mostStyle = Counter([dien['bigstyle'] for dien in ipeendata if haversine(lng1=dien["lng"],
                                                                                     lat1=dien["lat"],
                                                                                     lng2=wowDien["lng"],
                                                                                     lat2=wowDien[
                                                                                         "lat"]) <= radius and 'bigstyle' in dien]).most_common(
                1)[0][0]
        except:
            mostStyle = ""
        wowDien['mostStyle_Analyze'] = mostStyle
        ###############################################################################################################0320
        wowDien["NbusStation_Analyze"] = len([dien['stationName'] for dien in busData if "lng" in dien and haversine(lng1=dien["lng"],
                                                                                lat1=dien["lat"],
                                                                                lng2=wowDien["lng"],
                                                                                lat2=wowDien["lat"]) <= 500])
        wowDien["NconStore_Analyze"] = len([dien['name'] for dien in conStoreData if "lng" in dien and haversine(lng1=float(dien["lng"]),
                                                                                  lat1=float(dien["lat"]),
                                                                                  lng2=wowDien["lng"],
                                                                                  lat2=wowDien["lat"]) <= radius])
        wowDien["Nstar_Analyze"] = len([dien['name'] for dien in ipeendata
                                if '星巴' in dien['name']
                                and haversine(lng1=dien["lng"],
                                              lat1=dien["lat"],
                                              lng2=wowDien["lng"],
                                              lat2=wowDien["lat"]) <= radius])
        wowDien["Nmc_Analyze"] = len([dien['name'] for dien in ipeendata
                                if '麥當' in dien['name']
                                and haversine(lng1=dien["lng"],
                                              lat1=dien["lat"],
                                              lng2=wowDien["lng"],
                                              lat2=wowDien["lat"]) <= radius])
        wowDien["Nken_Analyze"] = len([dien['name'] for dien in ipeendata
                                if '肯德' in dien['name']
                                and haversine(lng1=dien["lng"],
                                              lat1=dien["lat"],
                                              lng2=wowDien["lng"],
                                              lat2=wowDien["lat"]) <= radius])
        wowDien["Nwa_Analyze"] = len([dien['name'] for dien in ipeendata
                                if '瓦城泰' in dien['name']
                                and haversine(lng1=dien["lng"],
                                              lat1=dien["lat"],
                                              lng2=wowDien["lng"],
                                              lat2=wowDien["lat"]) <= radius])
        ################################################################################################################0320
        ########################
        mapType = {'CooK BEEF!': '異國料理',
                   'hot 7': '燒烤類',
                   'ita義塔': '異國料理',
                   '乍牛': '日式料理',
                   '原燒': '燒烤類',
                   '品田牧場': '日式料理',
                   '夏慕尼': '燒烤類',
                   '沐越': '亞洲料理',
                   '王品': '異國料理',
                   '石二鍋': '鍋類',
                   '聚': '鍋類',
                   '舒果': '素食',
                   '莆田': '亞洲料理',
                   '藝奇': '日式料理',
                   '陶板屋': '日式料理',
                   '青花驕': '鍋類',
                   '麻佬大': '小吃',
                   'ＴＡＳＴｙ': '異國料理'}
        rangeCost = 1.4

        simDien = [dien['bigstyle'] for dien in ipeendata if haversine(lng1=dien["lng"],
                                                                       lat1=dien["lat"],
                                                                       lng2=wowDien["lng"],
                                                                       lat2=wowDien["lat"]) <= 500
                   and 'avgDailyNet' in wowDien
                   and dien['bigstyle'] == mapType[wowDien['Called']]
                   and dien['averagecost'] < ((wowDien['avgDailyNet'] / wowDien['avgDailyCustomer']) * rangeCost)
                   and dien['averagecost'] > ((wowDien['avgDailyNet'] / wowDien['avgDailyCustomer']) / rangeCost)]
        wowDien["NsimCostDien"] = len(simDien)
        # print(simDien)
        # print(wowDien['Called'])

        wowDien["Nwatson_Analyze"] = len([dien for dien in watsonsData
                                          if haversine(lng1=float(dien["lng"]),
                                                       lat1=float(dien["lat"]),
                                                       lng2=wowDien["lng"],
                                                       lat2=wowDien["lat"]) <= radius])
        ########################


        e = time.time()
    print(e-b)

    collection = client.rawData.wowprimediendata
    ids=[data.pop("_id") for data in wowDiensData]
    operations=[UpdateOne({"_id":idn},{'$set':data},upsert=True) for idn ,data in zip(ids,wowDiensData)]
    try:
        collection.bulk_write(operations ,ordered=False)
    except Exception as er:
        print(er)

    alldata=list(collection.find({}))

    client.close()
    
    mailTo(title="analyzeWowDataSuccess",mailAdds=["andy.yuan@wowprime.com"],message="分析完畢_耗時{}秒".format(e-b),whoSend='analyzeWowData')
except Exception as er:
    errorMsg=str(er)+"出錯位置:"+str(sys.exc_info()[2].tb_lineno)
    mailTo(title="analyzeWowDataFail",mailAdds=["andy.yuan@wowprime.com"],message=errorMsg,whoSend='analyzeWowData')
