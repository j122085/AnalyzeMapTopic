# -*- coding: UTF-8 -*- 
import requests
import json
import pymongo
import re
# res=requests.get("https://quality.data.gov.tw/dq_download_json.php?nid=32973&md5_url=52629fae1f1fed4ef81fcf706878dd80")
# x=json.loads(res.text)
try:

	res=requests.get("http://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=3AF951B6-534D-46CB-8276-E158B6D9EE41")
	datas=res.text.split("\r\n")
	titles=datas[0].split(",")
	x=[{title:value for title,value in zip(titles,data.split(","))} for data in datas[2:]]
	data=[{"add":add['site_id'].replace("　","").replace("\U000fffb5","五")+add['village'].replace(" ","").replace("\U000fffb5","五").replace("?","館"),'Nhuman':add['people_total']}for add in x[1:] if "site_id" in add]
	
	for i in data:
		try:
			i["bigadd"] = re.findall("(..[市|縣])(\w\w?\w?[區|市|鎮|鄉])",
									 i["add"])[0][0].replace("臺", "台")
			print(i['bigadd'],i['add'])
		except:
			i['bigadd'] = 0
		try:
			i["smalladd"] = re.findall("(..[市|縣])(\w\w?\w?[區|市|鎮|鄉])",
									   i["add"])[0][1]
		except:
			i["smalladd"] = 0
	client=pymongo.mongo_client.MongoClient("localhost",27017,username='j122085',password='850605')
	# #print(client.database_names())
	db=client.rawData
	#print(db.collection_names())
	collection=db.addressCoordinate
	Coordinate={add['add']:{"lat":add['lat'],'lng':add['lng']} for add in list(collection.find({}))}
	client.close()

	for add in data:
		try:
			add['lat']=Coordinate[add['add']]['lat']
			add['lng']=Coordinate[add['add']]['lng']
			add["_id"]=add.pop('add')
		except:
	#         #print(add['add'])
			pass
	Nhuman=[add for add in data if 'lat' in add]
	client=pymongo.mongo_client.MongoClient("localhost",27017,username='j122085',password='850605')
	db=client.rawData
	collection=db.Nhuman
	try:
		collection.drop()
		collection.insert_many(Nhuman,ordered=False)
	except:
		print("some data has same _id")
	client.close()
except Exception as e:
	import smtplib
	from email.message import EmailMessage
	msg = EmailMessage()
	msg.set_content("costPower "+str(e))
	msg['Subject'] = 'The costPower Crawler has some error'
	msg['From'] = "ServerNet"
	msg['To'] = 'andy.yuan@wowprime.com'
	with smtplib.SMTP('192.168.2.1',25) as s:
		s.send_message(msg)
