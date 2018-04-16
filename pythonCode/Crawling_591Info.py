from bs4 import BeautifulSoup as bs
import requests
import pymongo
import time
from pymongo import UpdateOne
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
import smtplib

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

mailTo("Crawler591InfoBegin",["andy.yuan@wowprime.com"],"go")

b=time.time()



header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
              "Accept-Encoding": "gzip, deflate, br",
              "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4",
              "Cache-Control": "max-age=0",
              "Connection": "keep-alive",
              "Cookie": "PHPSESSID=6bi7bnrv70rduoug42ptjdkrk3; new_rent_list_kind_test=1; T591_TOKEN=6bi7bnrv70rduoug42ptjdkrk3; _gat_tw591=1; _ga=GA1.3.1725785438.1503324510; _gid=GA1.3.659177335.1503324510; _gat=1; _dc_gtm_UA-97423186-1=1; c10f3143a018a0513ebe1e8d27b5391c=1; urlJumpIp=1; urlJumpIpByTxt=%E5%8F%B0%E5%8C%97%E5%B8%82; 591_new_session=eyJpdiI6IkhOelIwYUFrMU1KMmRON0NiTkxNN2c9PSIsInZhbHVlIjoiWUFcL2ZGN2U2eGVxNlpmVjZUVERWUDN6T0lFZFNvWUo0YjB6REEycjVES1BQVmFpVEhwcHpHZ3hKYlBMTUFpSjd2QUZkdnFuSERNSHY1ZURhVVh0dUh3PT0iLCJtYWMiOiJmY2VjMzNlNDhhODVjZGQ5YmY4YWMzYzU3MmUxNjUyYjgzN2NmYjM3NTg0MDcyM2IyN2FmNjVjMzdiMGY4OTBjIn0%3D; _ga=GA1.4.1725785438.1503324510; _gid=GA1.4.659177335.1503324510; _gat_UA-97423186-1=1",
              "Host": "rent.591.com.tw",
              "Upgrade-Insecure-Requests": "1",
              "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"
              }


try:
    client = pymongo.mongo_client.MongoClient("localhost", 27017, username='j122085', password='850605')
    # collection = client.rawData.wowprimeipeen


    #將舊原始資料確認網頁是否還存在、不存在就變更狀態soldout=1
    collectionInsert = client.rawData.info591 #放資訊的地方collection
    oldUrls={i['url'] for i in list(collectionInsert.find())}

    collection = client.rawData.websites591 #放新抓的網址的collection
    newUrls = set(collection.find()[0]['urls'])

    reUrls=oldUrls-newUrls #需review的Urls
    # print("有{}筆需review".format(len(reUrls)))
    dn=0
    for reUrl in reUrls:
        dn+=1
        if dn%25==0:
            time.sleep(5)
            # print("以review{}筆租屋".format(dn))
        count = 10
        res=""
        while count > 0:
            try:
                res = requests.get(reUrl, headers=header, timeout=2)
                count = 0
                break
            except Exception as e:
                time.sleep(count * 0.1)
                count -= 1
        if res!="" and res.status_code==200 and '您查詢的物件不存在，可能已關閉或者被刪除' in res.text:
            collectionInsert.update_one({"url":reUrl},{'$set':{'soldout':"1"}})
            print(reUrl,'該房已soldout')
        res.close()



    #更新資料
    
    n=0
    info591s=[]
    for url in newUrls:
        n+=1
        if n%25==0:
            time.sleep(5)
            # print("已完成{}筆資料".format(n))
            ids=[data["url"].split("-")[-1].split(".")[0] for data in info591s]
            operations=[UpdateOne({"_id":idn},{'$set':data},upsert=True) for idn ,data in zip(ids,info591s)]
            try:
                collectionInsert.bulk_write(operations ,ordered=False)
            except Exception as er:
                print(er)

        count = 10
        while count > 0:
            try:
                res = requests.get(url, headers=header, timeout=2)
                count = 0
                break
            except Exception as e:
                time.sleep(count * 0.1)
                count -= 1

        soup=bs(res.text,"lxml")
        try:
            rentDict = {}
            info = soup.select("#propNav > a['href']")
            types = info[2].text
            area = info[3].text
            city = info[4].text
            title = soup.select('.houseInfoTitle')[0].text
            # 標題
            address = soup.select('span.addr')[0].text
            # 地址
            price = soup.select('div.price > i')[0].text.split(' 元/月')[0].replace(',', '')
            # 租金
            houseInfo = soup.select('ul.attr > li')
            if info[2].text == "車位":
                square = houseInfo[0].text.split('\xa0')[3].split('坪')[0]
                floor = ""
                style = ""

            elif houseInfo[0].text.split('\xa0')[0] == "坪數":

                if houseInfo[1].text.split('\xa0')[0] == "權狀坪數":
                    square = houseInfo[0].text.split('\xa0')[3].split('坪')[0]
                    floor = houseInfo[2].text.split('\xa0')[3].split('/')[0]
                    totfloor = houseInfo[2].text.split('\xa0')[3].split('/')[1]
                    style = houseInfo[3].text.split('\xa0')[3]
                else:
                    square = houseInfo[0].text.split('\xa0')[3].split('坪')[0]
                    floor = houseInfo[1].text.split('\xa0')[3].split('/')[0]
                    totfloor = houseInfo[1].text.split('\xa0')[3].split('/')[1]
                    style = houseInfo[2].text.split('\xa0')[3]

            elif houseInfo[0].text.split('\xa0')[0] == "格局":
                if houseInfo[2].text.split('\xa0')[0] == "權狀坪數":
                    square = houseInfo[1].text.split('\xa0')[3].split('坪')[0]
                    floor = houseInfo[3].text.split('\xa0')[3].split('/')[0]
                    totfloor = houseInfo[3].text.split('\xa0')[3].split('/')[1]
                    style = houseInfo[4].text.split('\xa0')[3]
                else:
                    square = houseInfo[1].text.split('\xa0')[3].split('坪')[0]
                    floor = houseInfo[2].text.split('\xa0')[3].split('/')[0]
                    totfloor = houseInfo[2].text.split('\xa0')[3].split('/')[1]
                    style = houseInfo[3].text.split('\xa0')[3]

            else:
                None
            seller = soup.select('.avatarRight')[0].text.strip().replace("（", '(').split('(')[0]
            identity = \
            soup.select('.avatarRight')[0].text.strip().replace("（", '(').replace("）", ')').split(')')[0].split('(')[1]
            if identity == "屋主聲明：仲介勿擾":
                identity = "屋主"
            elif identity == "仲介，收取服務費" or "仲介，不須服務費":
                identity = "仲介"
            else:
                None

            phoneSoup = soup.select_one("span.num")

            if len(phoneSoup) == 1 and phoneSoup.text == "":
                for img in phoneSoup:
                    phone = img['src']
                soldout = 0
            elif len(phoneSoup) == 1 and phoneSoup.text != "":
                phone = phoneSoup.text
                soldout = 0

            else:
                phone = ""
                soldout = 1


            if len(soup.select('div.lifeBox > p')) == 2:
                traffic = soup.select('div.lifeBox > p')[1].text.replace("附近交通：", "").split('； ')
            else:
                traffic = ""
            rentDict['url'] = url
            rentDict['title'] = title
            rentDict['seller'] = seller
            rentDict['identity'] = identity
            rentDict['phone'] = "https:"+phone
            rentDict['price'] = int(price)
            rentDict['type'] = types
            rentDict['floor'] = floor
            rentDict['totfloor'] = totfloor
            rentDict['square'] = float(square)
            rentDict['address'] = address
            rentDict['city'] = city
            rentDict['area'] = area
            rentDict['style'] = style
            rentDict['traffic'] = str(traffic)
            rentDict['soldout'] = str(soldout)
            info591s.append(rentDict)

        except Exception as e:
            print('There is get_content trouble in {},{} '.format(url, e))
            collectionInsert.update_one({"url":url},{'$set':{'soldout':"1"}})

    ids=[data["url"].split("-")[-1].split(".")[0] for data in info591s]
    operations=[UpdateOne({"_id":idn},{'$set':data},upsert=True) for idn ,data in zip(ids,info591s)]
    try:
        collectionInsert.bulk_write(operations ,ordered=False)
    except Exception as er:
        print(er)
    e=time.time()
    print(int(e-b))
    mailTo("Crawler591InfoReport",["andy.yuan@wowprime.com"],"完成{}筆review，完成{}筆更新，耗時{}秒".format(len(reUrls),len(newUrls),int(e-b)))
    
except Exception as er:
    errorstr="出錯"+str(er)+"出錯位置:"+str(sys.exc_info()[2].tb_lineno)
    mailTo("Crawler591Info_error",["andy.yuan@wowprime.com"],errorstr)
