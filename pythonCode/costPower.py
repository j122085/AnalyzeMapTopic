# -*- coding: UTF-8 -*-

import requests
import pymongo

try:
	res=requests.get("https://sip.einvoice.nat.gov.tw/ods-main/ODS308E/download/691C0280-CEFB-488F-9E71-6AA4F39A41CD/8/1124193D-09F5-4711-AB9A-01848E3B88E4/8/?fileType=csv")
	x=res.text
	keys=x.replace('"',"").replace("\u3000","").replace("\U000fffb4","").replace("\r","").split("\n")[0].split(",")
	values=[data.replace("\u3000","")
			.replace("\U000fffb4","")
			.replace("\U000fb56f","塭")
			.replace("\r","")
			.split(",") for data in x.replace('"',"").split("\n")[1:]]
	datalist=[]
	for valueList in values:
		data={}
		for key,value in zip(keys,valueList):
			data[key]=value
		datalist.append(data)
	dataFinal=[]
	for i in datalist:
		data={}
		if i.get('主行業別',"")=='餐飲業' and i.get('年度',"")=='2017' and i.get("消費熱度計算來源","")=="電子發票":
			data['add']=i['縣市']+i['鄉鎮市區']+i['村里']
			data['bigadd'] = i['縣市'].replace("臺", "台")
			data['smalladd'] = i['鄉鎮市區']
			data['costPower']=i['銷售額指標']
			dataFinal.append(data)
	
	print([i['bigadd'] for i in dataFinal])		
	client=pymongo.mongo_client.MongoClient("localhost",27017,username='j122085',password='850605')
	# print(client.database_names())
	db=client.rawData
	# print(db.collection_names())
	collection=db.addressCoordinate
	Coordinate={add['add']:{"lat":add['lat'],'lng':add['lng']} for add in list(collection.find({}))}
	client.close()

	for add in dataFinal:
		try:
			add['lat']=Coordinate[add['add']]['lat']
			add['lng']=Coordinate[add['add']]['lng']
			add["_id"]=add.pop('add')
		except:
	#        print(add['add'])
			pass
	costPower=[add for add in dataFinal if 'lat' in add]
	client=pymongo.mongo_client.MongoClient("localhost",27017,username='j122085',password='850605')
	db=client.rawData
	collection=db.CostPower
	try:
		collection.drop()
		collection.insert_many(costPower,ordered=False)
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
