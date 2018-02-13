import json
import os
import requests
from bs4 import BeautifulSoup as bs
import time
import pymongo
from pymongo import MongoClient
# from pymongo import UpdateOne#0125
import smtplib
from email.message import EmailMessage
b=time.time()

try:
	msg = EmailMessage()
	msg.set_content(str(time.strftime("%Y/%m/%d %H:%M")))
	msg['Subject'] = 'The IpeenWebsite Crawler has started to run'
	msg['From'] = "ServerNet"
	msg['To'] = 'andy.yuan@wowprime.com'
	with smtplib.SMTP('192.168.2.1',25) as s:
		s.send_message(msg)




	#確認檔案資料夾是否存在
	if not os.path.exists('../data'):
		os.makedirs('../data')
		
	#抓取網址(愛評網全台餐飲店)
	URL="http://www.ipeen.com.tw/search/taiwan/000/0-0-0-0/%20/?bar=1"


	#抓取總頁數
	res=requests.get(URL+"&p=1")
	soup=bs(res.text,"lxml")
	res.close()
	page=int(soup.select("#search > article > hgroup > h2 > b")[0].text)//15
	#print(str(page)+"pages(all)")

	#初始網址set(不會重複)、抓取起始頁
	WebsiteSet=set()
	pagebegin=1


	#從過去抓取到的頁面開始，繼續抓取
	if os.path.exists('../data/beginpage.txt'):
		with open("../data/beginpage.txt") as p:
			pagebegin=int(p.read())

	#print("開始頁%s"%pagebegin)

	# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}


	#抓取各店家的id:網址
	#會累積的變數>>i WebsiteSet
	for i in range(pagebegin+1,page+1):
	#         try:
	#             res=requests.get(URL+"&p="+str(i))
	#             if "RedisException" in res.text:
	#                 #print("requests太頻繁被卡，睡兩分鐘")
	#                 time.sleep(120)
	#                 res=requests.get(URL+"&p="+str(i))
	#         except:
	#             #print("requests逾時，睡兩分鐘")
	#             time.sleep(120)
	#             res=requests.get(URL+"&p="+str(i))
		res = None
		while res is None:
			try:
				res=requests.get(URL+"&p="+str(i))
				while "RedisException" in res.text or "目前系統忙碌中" in res.text:
					#print("requests太頻繁被卡，睡兩分鐘")
					time.sleep(120)
					res=requests.get(URL+"&p="+str(i))
			except:
				#print("requests逾時，睡兩分鐘")
				time.sleep(120)


		if res.status_code==200:
			soup=bs(res.text,'lxml')
			try:
				dienlist=soup.select("article.serMain > div.result > section > article.serItem > div > h3")
			except:
				#print("本頁已死")
				continue

	#         dienlist=[dien for dien in dienlist  if not dien.select_one("span.status")]#去除搬遷或關店狀態的店家>改全抓
			dienlist=["http://www.ipeen.com.tw"+dien.select_one("a")["href"].split("-")[0] for dien in dienlist 
					  if dien.select_one("a")["data-action"]!="ad_shop"]#去除廣告店家，並留下網址>改不留店名
			WebsiteSet.update(dienlist)

			#每抓取15頁的網址，睡5秒以免被ban，並將資料已json格式儲存一次
			if i%15==0:
				#print("-----\n已抓取第%s頁"%i)
				#print(len(WebsiteSet))

				#-----------------------------------------------
	#                 with open("../data/WebsiteSet.json","w") as f:
	#                     json.dump(websitedict,f)
				#連Mongodb
				client = pymongo.MongoClient('localhost', 27017,username='j122085',password='850605')
				#連DB名
				db=client['rawData']
				#秀DB內的collection list
				collection = db.ipeenWebsite
				try:
	#                     operations=[UpdateOne({"_id":Website.split("/")[-1]},
	#                                           {'$set':{"website":Website}},
	#                                           upsert=True) 
	#                                 Website in WebsiteSet]
	#                     collection.bulk_write(operations)
					# 如果資料內有相同_id會報錯，但所有非相同_id的資料都會insert
					collection.insert_many([{"_id":Website.split("/")[-1],"website":Website}for Website in WebsiteSet], ordered=False)
				except:
					pass
					#print("some data has same _id")
				client.close()
				WebsiteSet=set()
				#-----------------------------------------------    
				with open("../data/beginpage.txt","w") as p:
					p.write(str(i))
				time.sleep(20)  
		else:
			#無法進入頁面則顯示目前網址個數
			#print("status_code"+str(res.status_code))
			#print(len(WebsiteSet))
			#print("request出錯，睡30秒")
			time.sleep(30)
	#         websitedict={Website.split("/")[-1]:Website for Website in WebsiteSet}#改存{id:網址}格式
	#         with open("./data/WebsiteSet.json","w") as f:
	#             json.dump(websitedict,f)
	#         with open("./data/beginpage.txt","w") as p:
	#             p.write(str(i))


	#將所有資料抓取完畢後，在儲存最後一次        
	#連Mongodb
	client = pymongo.MongoClient('localhost', 27017,username='j122085',password='850605')
	#連DB名
	db=client['rawData']
	#秀DB內的collection list
	collection = db.ipeenWebsite
	try:
		collection.insert_many([{"_id":Website.split("/")[-1],"website":Website}for Website in WebsiteSet], ordered=False)
	except:
		pass
		#print("some data has same _id")
	NData=collection.count()
	client.close()
	with open("../data/beginpage.txt","w") as p:
		p.write(str(0))
	#print("已抓取完畢")
	#兩週抓一次


	e=time.time()

	msg = EmailMessage()
	msg.set_content("\n".join([str(time.strftime("%Y/%m/%d %H:%M")),
							   "use {} second".format(round(e-b)),
							   "we crawled {} datas".format(NData)]))
	msg['Subject'] = 'The IpeenWebsit Crawler is finished'
	msg['From'] = "ServerNet"
	msg['To'] = 'andy.yuan@wowprime.com'
	with smtplib.SMTP('192.168.2.1',25) as s:
		s.send_message(msg)
except Exception as e:
	msg = EmailMessage()
	msg.set_content("IpeenWebsite Crawler "+str(e))
	msg['Subject'] = 'The IpeenWebsite Crawler has some error'
	msg['From'] = "ServerNet"
	msg['To'] = 'andy.yuan@wowprime.com'
	with smtplib.SMTP('192.168.2.1',25) as s:
		s.send_message(msg)
