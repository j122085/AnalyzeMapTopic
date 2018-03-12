import pymssql
import googlemaps
import json
import time
import pymongo
from pymongo import UpdateOne
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
import smtplib
import re

b = time.time()


def mailTo(title, mailAdds, message, whoSend='AutoAddInsurance'):
    msg = MIMEMultipart()
    sender = whoSend
    subject = title
    body = message
    msg['From'] = sender
    msg['To'] = ','.join(mailAdds)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    # print text
    # Send the message via our SMTP server
    s = smtplib.SMTP('192.168.2.1', 25)
    s.sendmail(sender, mailAdds, text)
    s.quit()


try:
    # mssql撈店家資料
    conn = pymssql.connect(server='datacenter.wowprime.com', user='python',
                           password='12321', database='WangGroup')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM [WangGroup].[dbo].[StoreDetail_View] WHERE\
                   right(rtrim(StoreNo),2) <> '00'")
    wowprimeDienData = cursor.fetchall()

    # mssql撈欄位名稱
    cursor.execute("SELECT * FROM sys.columns WHERE object_id = OBJECT_ID('dbo.StoreDetail_View')")
    cols = [i[1] for i in cursor.fetchall()]
    conn.close()
    # 將欄位名稱+店家資料做成dict以便編輯
    wowprimeDienDatalist = []
    for dien in wowprimeDienData:
        diendict = {}
        for c, d in zip(cols, dien):
            if type(d) == str:
                d = d.strip()
            elif type(d) != int:
                d = str(d)
            diendict[c] = d
        wowprimeDienDatalist.append(diendict)
    # 用googlemapApi將地址轉換成經緯度座標(有一日限制、速度限制)
    gmaps = googlemaps.Client(key='AIzaSyAF9GKxqgmgDEW_h7M4TtM5CbkK03xnS0E')
    for wowprimeDienData in wowprimeDienDatalist:
        address = wowprimeDienData['Address']
        try:
            if 'lat' not in wowprimeDienData.keys():
                # 關閉的店、店號有A的、大陸的店都不需要做
                if wowprimeDienData['CloseDate'] == "None" \
                        and "A" not in wowprimeDienData['StoreNo'] \
                        and "B" not in wowprimeDienData['StoreNo'] \
                        and wowprimeDienData['StoreNo'][0] != '3' \
                        and wowprimeDienData['StoreNo'][:2] != '19' \
                        and wowprimeDienData['StoreNo'][:2] != '41':
                    geocode_result = gmaps.geocode(address)
                if geocode_result == []:
                    geocode_result = gmaps.geocode(address[:11])
                wowprimeDienData['lat'] = geocode_result[0]['geometry']['location']['lat']
                wowprimeDienData['lng'] = geocode_result[0]['geometry']['location']['lng']
                print(wowprimeDienData['Corporation_ch'])
                time.sleep(1.5)

        except Exception as e:
            print(e)
            print(wowprimeDienData['Corporation_ch'] + "-" + wowprimeDienData['Address'] + "無經緯度資料")

    datas = wowprimeDienDatalist
    # 計算營收、顧客量、客量
    conn = pymssql.connect(server='UISDB2.wowprime.com', user='admin',
                           password='2802836', database='DMart')
    cursor = conn.cursor()

    cursor.execute("""SELECT sum([NetTotal]) ,StoreNo
                          FROM [DMart].[dbo].[BI_ORA_FACTV_SalesDaily]
                          WHERE YEAR([TradeDate])=YEAR(getdate())-1 and StoreStatus='營業中' 
                          group by [StoreNo]""")
    DienSaleInfo = cursor.fetchall()
    dienYearRevenues = {i[1]: int(i[0]) for i in DienSaleInfo}

    newDatas = []
    n = 0
    for data in datas:
        getData = {}
        getData['Address'] = data['Address']
        getData['AreaManager'] = data['AreaManager']
        getData['Called'] = data['Called']
        getData['CareerName'] = data['CareerName']
        getData['CareerNo'] = data['CareerNo']
        getData['Chef'] = data['Chef']
        getData['CodeId'] = data['CodeId']
        getData['CorporationId'] = data['CorporationId']
        getData['Corporation_ch'] = data['Corporation_ch']
        getData['CreateDate'] = data['CreateDate']
        getData['CorporationId'] = data['CorporationId']
        getData['ItemName'] = data['ItemName']
        getData['CorporationId'] = data['CorporationId']
        getData['Manager'] = data['Manager']
        getData['PlaceNo'] = data['PlaceNo']
        getData['Phone'] = data['Phone']
        getData['PlaceNo'] = data['PlaceNo']
        getData['StoreName'] = data['StoreName']
        getData['StoreNo'] = data['StoreNo']
        try:
            getData['lat'] = data['lat']
            getData['lng'] = data['lng']
        except:
            pass
        getData['_id'] = data['StoreNo']
        getData['CloseDate'] = data['CloseDate']
        try:
            getData["bigadd"] = re.findall("(\w\w[市|縣])(\w\w?\w?[區|市|鎮|鄉])",
                                           data["Address"])[0][0]
        except:
            try:
                getData["bigadd"] = re.findall("(\w\w[市|縣])",
                                               data["Address"])[0]
            except:
                getData['bigadd'] = 0
        try:
            getData["smalladd"] = re.findall("(..[市|縣])(\w\w?\w?[區|市|鎮|鄉])",
                                             data["Address"])[0][1]
        except:
            try:
                getData["smalladd"] = re.findall("(\w\w?\w?[區|市|鎮|鄉])",
                                                 data["Address"])[0].replace("市", "區")
            except:
                getData["smalladd"] = 0
        # 每家店的平均淨額、顧客量、客量
        if data['CloseDate'] == "None" and "A" not in data['StoreNo'] and "B" not in data['StoreNo'] and data['StoreNo'][0]!= '3':
            cursor.execute("""SELECT avg([NetTotal])
                              ,avg([CustomerAmtTotal])
                              ,avg([MealTotal])
                              FROM [DMart].[dbo].[BI_ORA_FACTV_SalesDaily]
                              WHERE StoreNo=""" + data['StoreNo'] + """ and [TradeDate]>(getdate()-90) and StoreStatus='營業中'
                              group by [StoreNo]""")
            DienSaleInfo = cursor.fetchall()
            try:
                getData['avgDailyNet'] = round(DienSaleInfo[0][0])
                getData['avgDailyCustomer'] = round(DienSaleInfo[0][1])
                getData['avgDailyMeal'] = round(DienSaleInfo[0][2])
            except:
                pass

            try:
                getData['lastYearRevenue'] = dienYearRevenues[data['StoreNo']]
            except:
                pass
        newDatas.append(getData)
    conn.close()

    # 將資料upsert進mongoDB裡面，以_id為上船索引
    client = pymongo.MongoClient('localhost', 27017, username="j122085", password="850605")
    #     client=pymongo.MongoClient('192.168.1.113', 27017,username="j122085",password="850605")

    db = client['rawData']
    db.collection_names()
    collection = db.wowprimediendata
    ids = [data.pop("_id") for data in newDatas]
    operations = [UpdateOne({"_id": idn}, {'$set': data}, upsert=True) for idn, data in zip(ids, newDatas)]
    try:
        collection.bulk_write(operations, ordered=False)
    except:
        print(e)
    # collection.drop()
    # collection.insert_many(newDatas,ordered=False)
    e = time.time()
    print(e - b)
    client.close()
    mailTo(title="transDataToMongoSuccess", mailAdds=["andy.yuan@wowprime.com"], message="轉換成功_耗時{}秒".format(e - b),
           whoSend='mssqlWowDataToMongoDB')

except Exception as e:
    errorMsg = str(e) + "出錯位置:" + str(sys.exc_info()[2].tb_lineno)
    mailTo(title="transDataToMongoError", mailAdds=["andy.yuan@wowprime.com"], message=errorMsg,
           whoSend='mssqlWowDataToMongoDB')