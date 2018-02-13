import json
import requests
import os
from bs4 import BeautifulSoup as bs    
import time
import pymongo
import re
from pymongo import UpdateOne#0125
from collections import Counter
import smtplib
from email.message import EmailMessage


try:
	b=time.time()
	msg = EmailMessage()
	msg.set_content(str(time.strftime("%Y/%m/%d %H:%M")))
	msg['Subject'] = 'The IpeenInfo Crawler has started to run'
	msg['From'] = "ServerNet"
	msg['To'] = 'andy.yuan@wowprime.com'
	with smtplib.SMTP('192.168.2.1',25) as s:
		s.send_message(msg)
		
	#確認共有幾個網址需要抓
	#連Mongodb
	client = pymongo.MongoClient('localhost', 27017,username='j122085',password='850605')
	#連DB名
	db=client['rawData']
	#秀DB內的collection list
	#print(db.collection_names())
	collectionWeb = db.ipeenWebsite
	ipeenWebsite={dien['_id']:dien["website"] for dien in list(collectionWeb.find({}))}

	#print("共有%s資料要抓取"%len(ipeenWebsite))
	collectionInfo = db.ipeenInfo
	dienInfo=list(collectionInfo.find({}))
	client.close()
				  
	dienset=set()         
	#if len(dienInfo)!=0:
	#    dienset=set([dien["_id"] for dien in dienInfo])

	n=0
	#將每個網址的網頁抓下來，每30頁睡5秒防ban
	dienlist=[]
	for i in ipeenWebsite:
		if int(i) not in dienset:
	#         e=time.time()
	#         print(int(e-b))
	#         print("連接前")
			try:
				res = None
				while res is None:
					try:
						res=requests.get(ipeenWebsite[i])
						while "RedisException" in res.text or "目前系統忙碌中" in res.text:
							#print("requests太頻繁被卡，睡兩分鐘")
							time.sleep(120)
							res=requests.get(ipeenWebsite[i])
					except:
						#print("requests逾時，睡兩分鐘")
						time.sleep(120)
				if "很抱歉，找不到此頁面！" in res.text:
					print("{}，該頁已死".format(i))
					continue
				if res.status_code==200:
					n+=1
		#             e=time.time()
		#             print(int(e-b))
		#             print("已連接")
					if n%20==0:
						client = pymongo.MongoClient('localhost', 27017,username='j122085',password='850605')
						db=client['rawData']
						collectionInfo = db.ipeenInfo
						try:
							#0125----------------------------
							ids=[data.pop("_id") for data in dienlist]
							operations=[UpdateOne({"_id":idn},{'$set':data},upsert=True) for idn ,data in zip(ids,dienlist)]
							collectionInfo.bulk_write(operations)
							#0125----------------------------
		#                     collectionInfo.insert_many(dienlist,ordered=False)
						except:
							print("RRRRRRRRRRRRRRRRRRRRRR")#0125
		#                     print("some data has same _id")
						dataN=collectionInfo.count()#0125
						client.close()
						#print("目前有{}筆資料".format(dataN))#0125
		#                 print("目前有{}筆資料".format(len(dienInfo)+n))
						dienlist=[]
						time.sleep(10)
					diendata={}
					soup=bs(res.text,"lxml")
					info=soup.select_one("#shop-header > div.info")

					diendata["_id"]=int(i)#id
					diendata["name"]=info.find('span', attrs={'itemprop': 'name'}).text.replace('"',"")
					try:
						diendata['othername']=re.findall("\((\w*[店|館|門市|百貨|街|夜市|商場|時代|廣場|中心|三越|大學|中|區|高鐵])\)",diendata['name'])[0]
					except:
						diendata['othername']=0


					diendata["bigstyle"]=soup.find('a', attrs={'data-label': '詳細資訊_大分類'}).text
					diendata["smallstyle"]=info.find('a', attrs={'data-label': '上方小分類'}).text

					try:
						diendata["averagecost"]=int(re.findall("本店均消 +([0-9]+) +元",info.select_one('p.cost.i').text)[0])
					except:
						diendata["averagecost"]=0
					try:
						diendata["tele"]=info.find('a', attrs={'data-label': '上方電話'}).text.replace("-","").replace(")","").replace("(","").replace(" ","")#tele
					except:
						diendata["tele"]=0
					try:
						diendata["address"]=info.find('a', attrs={'data-label': '上方地址'}).text.replace("\n"," ").strip()
		#                 diendata["address"]=re.findall("..[市|縣].+[區|市|鎮|鄉].+[路|街|地段|巷|鎮][0-9]+[-|之]?[0-9]*?[號|巷|弄]?[0-9]*[號|巷|弄|樓]",
		#                        info.find('a', attrs={'data-label': '上方地址'}).text)[0]#add
					except:
						diendata["address"]=0
					#0116新增=================================================
					try:
						diendata["bigadd"] = re.findall("(..[市|縣])(\w\w?\w?[區|市|鎮|鄉])",diendata["address"])[0][0]
						diendata["smalladd"] = re.findall("(..[市|縣])(\w\w?\w?[區|市|鎮|鄉])",diendata["address"])[0][1]
					except:
						diendata["bigadd"]=0
						diendata["smalladd"]=0
					#0116新增=================================================
					try:
						diendata["lat"]=float(re.findall("\/c=([0-9]+\.[0-9]+)\,([0-9]+\.[0-9]+)\/z=",
													   info.find('a', attrs={'data-label': '上方地址'})["href"])[0][0])#lat.lng
					except:
						diendata["lat"]=0
					try:
						diendata["lng"]=float(re.findall("\/c=([0-9]+\.[0-9]+)\,([0-9]+\.[0-9]+)\/z=",
													   info.find('a', attrs={'data-label': '上方地址'})["href"])[0][1])#lat.lng
					except:
						diendata["lng"]=0
					try:
						diendata["Ncomment"]=int(re.findall("會員分享文 \(([0-9]+)\)",soup.text)[0])#Ncomment
					except:
						diendata["Ncomment"]=0

					#第四版變更---------------------
					diendata["url"]=ipeenWebsite[i]
		#             commentPage=int(diendata["Ncomment"]/5)+1
		#             peenlist=[]
		#             for i in range(1,commentPage+1):
		#                 url2=diendata["url"]+'/comments?p='+str(i)
		#                 res2=requests.get(url2)
		#                 n+=1
		#                 #每90筆requests資料儲存一次
		#                 if n%90==0:
		#                     with open(savePath,"w") as d:
		#                         json.dump(dienlist,d)
		#                     print("已存%s筆店家資料"%k)
		#                 #每45筆睡5秒，以防ban
		#                 if n%30==0:
		#                     e=time.time()
		#                     print("已執行%s秒"%int(e-b))
		#                     time.sleep(5)
		#                 if k%1000==0:
		#                     with open("..\data\diendataURL2\%s.json"%k,"w") as d:
		#                         json.dump(dienlist,d)
		#                     print("%s筆資料已備分"%k)
		#                 if res2.status_code == 200:
		#                     soup2=bs(res2.text,'lxml')
		#                     res2.close()
		#                     pagepeenlist=['http://www.ipeen.com.tw'+i['href'] for i in soup2.select("p.summary > a") 
		#                                   if "checkin" not in i['href']]
		#                     peenlist+=pagepeenlist
					peenlist=['http://www.ipeen.com.tw'+i['href'] for i in soup.select("p.summary > a") 
										  if "checkin" not in i['href']]
					diendata["comments"]=peenlist
					#第四版變更---------------------  
					diendata["ipeenscore"]=int(info.select_one("span.score-bar.large > meter")['value'])#ipeenscore
					if "已歇業" in info.select_one("h1").text:
						diendata["status"]="結束營業"
					elif "已搬遷" in info.select_one("h1").text:
						diendata["status"]="已搬遷"
					else:
						diendata["status"]="正常營業"
					diendata["viewcount"]=int(re.findall("共([0-9]+)人瀏覽([0-9]+)人收藏",info.select_one("div.scalar").text.
							   replace(",","").replace("\n","").replace(" ",""))[0][0])#viewcount
					diendata["collecount"]=int(re.findall("共([0-9]+)人瀏覽([0-9]+)人收藏",info.select_one("div.scalar").text.
							   replace(",","").replace("\n","").replace(" ",""))[0][1])#collecount
					diendata["reviewdate"]=re.findall("更新時間(\d{4}\/\d{2}\/\d{2})",soup.select_one("div#shop-details").text.
							   replace("\n","").replace(" ",""))[0]#renewdate
					dienlist.append(diendata)
					res.close()
		#             e=time.time()
		#             print(int(e-b))
		#             print("已爬取")
		#             print(i)
				else:
					#print(res.status_code)
					#print(i+"失敗")
					res.close()
					#print("request出錯，睡30秒")
					time.sleep(30)
			except:
				print("{}，該頁已死".format(i))
				continue
		#過去抓取過的網頁直接跳過
		else:
	#         print(i+"已抓取跳過")
			pass
			
	client = pymongo.MongoClient('localhost', 27017,username='j122085',password='850605')
	db=client['rawData']
	collectionInfo = db.ipeenInfo
	try:
		#0125----------------------------
		ids=[data.pop("_id") for data in dienlist]
		operations=[UpdateOne({"_id":idn},{'$set':data},upsert=True) for idn ,data in zip(ids,dienlist)]
		collectionInfo.bulk_write(operations)
		#0125----------------------------
	#                     collectionInfo.insert_many(dienlist,ordered=False)
	except:
		print("RRRRRRRRRRRRRRRRRRRRRR")#0125
	#                     print("some data has same _id")
	dataN=collectionInfo.count()#0125
	#0126-------------------------------------------------------------每次抓取完畢後，統計類型
	ipeenData=list(collectionInfo.find({}))
	bigStyleCount = dict(Counter([dien['bigstyle'] for dien in ipeenData if dien['status'] == "正常營業"
													 and dien['lat'] > 18
													 and dien['lat'] < 27
													 and dien['lng'] < 125
													 and dien['lng'] > 117
													 and dien['bigadd'] != 0
													 and dien['smalladd'] != 0]))
	smallStyleCount = dict(Counter([dien['smallstyle'] for dien in ipeenData if dien['status'] == "正常營業"
													 and dien['lat'] > 18
													 and dien['lat'] < 27
													 and dien['lng'] < 125
													 and dien['lng'] > 117
													 and dien['bigadd'] != 0
													 and dien['smalladd'] != 0]))

	nowdate=time.strftime("%Y%m%d", time.localtime())
	bigStyleCount['_id']=nowdate
	smallStyleCount['_id']=nowdate
	try:
		db.smallStyleCount.insert_one(smallStyleCount)
		db.bigStyleCount.insert_one(bigStyleCount)
	except:
		pass
	#0126-------------------------------------------------------------
	client.close()
	#print("共有{}筆資料".format(dataN))


	e=time.time()

	msg = EmailMessage()
	msg.set_content("\n".join([str(time.strftime("%Y/%m/%d %H:%M")),
							   "use {} second".format(round(e-b)),
							   "we crawled {} datas".format(dataN)]))
	msg['Subject'] = 'The IpeenInfo Crawler is finished'
	msg['From'] = "ServerNet"
	msg['To'] = 'andy.yuan@wowprime.com'
	with smtplib.SMTP('192.168.2.1',25) as s:
		s.send_message(msg)
except Exception as e:
	msg = EmailMessage()
	msg.set_content("IpeenInfo Crawler "+str(e))
	msg['Subject'] = 'The IpeenInfo Crawler has some error'
	msg['From'] = "ServerNet"
	msg['To'] = 'andy.yuan@wowprime.com'
	with smtplib.SMTP('192.168.2.1',25) as s:
		s.send_message(msg)
