import requests
from bs4 import BeautifulSoup as bs
import json
import time
import os
import sys
import smtplib
from email.message import EmailMessage
b=time.time()


try:
	msg = EmailMessage()
	msg.set_content(str(time.strftime("%Y/%m/%d %H:%M")))
	msg['Subject'] = 'The Hr Crawler has started to run'
	msg['From'] = "ServerNet"
	msg['To'] = 'andy.yuan@wowprime.com'
	with smtplib.SMTP('192.168.2.1',25) as s:
		s.send_message(msg)


	#當天日期
	nowdate=time.strftime("%Y%m%d", time.localtime())

	#104API網址，參數設定完成
	URL="http://www.104.com.tw/i/apis/jobsearch.cfm?fmt=8&cols=JOB,JOB_ADDR_NO_DESCRIPT,NAME,JOB_ADDRESS,JOBCAT_DESCRIPT,PRODUCT,APPEAR_DATE,SAL_MONTH_LOW,SAL_MONTH_HIGH,LAT,LON&pgsz=2000&order=5&cat=2006001000&asc=1"
	#待加入area=60010XX(市代號)0XX(區代號)

	#市代號(1-14)
	bigAreaList=[len(str(i))<2 and "0"+str(i) or str(i) for i in range(1,20+1)]
	#區代號(1-29)
	samllAreaList=[len(str(i))<2 and "0"+str(i) or str(i) for i in range(1,29+1)] 

	#資料夾建立
	savedir="../data/104json"
	if not os.path.exists(savedir):
		os.makedirs(savedir)
	#當日資料夾建立
	if not os.path.exists(savedir+"/"+nowdate):
		os.makedirs(savedir+"/"+nowdate)

	#我們有興趣的職業
	some={'中餐廚師',
	 '儲備幹部',
	 '其他類廚師',
	 '工讀生',
	 '店長／賣場管理人員',
	 '日式廚師',
	 '櫃檯接待人員',
	 '洗碗人員',
	 '營養師',
	 '物管／資材',
	 '生鮮人員',
	 '經營管理主管',
	 '行政助理',
	 '西餐廚師',
	 '西點／蛋糕師',
	 '記帳／出納／一般會計',
	 '調酒師／吧台人員',
	 '連鎖店管理人員',
	 '門市／店員／專櫃人員',
	 '領班',
	 '食品研發人員',
	 '食品衛生管理師',
	 '飯店工作人員',
	 '飯店或餐廳主管',
	 '餐廚助手',
	 '餐飲服務生',
	 '麵包師'}



	def get104JsonData(allpage,url):
		'''爬取這個網頁的json檔'''

		HRdata104=[]
		for i in range(1,allpage+1):
			alldata=None
			while alldata==None:
				try:
					res=requests.get(url+"&page=%s"%i)
					if res.status_code==200:
						alldata=json.loads(res.text)#直到alldata得到資料為止，不斷
						HRdata104+=[case for case in alldata['data'] if case["NAME"]!="104外包網" 
									and case['JOBCAT_DESCRIPT'].split("@")[0] in some]
				except:
					time.sleep(15)
			res.close()
			time.sleep(1.5)
			#print(i)
		for dien in HRdata104:
			dien['JOBCAT_DESCRIPT']=dien['JOBCAT_DESCRIPT'].split("@")[0]
			try:
				dien['LAT']=float(dien['LAT'])
				dien['LON']=float(dien['LON'])
			except:
				dien['LAT']=0.0
				dien['LON']=0.0
			dien['SAL_MONTH_HIGH']=int(dien['SAL_MONTH_HIGH'])
			dien['SAL_MONTH_LOW']=int(dien['SAL_MONTH_LOW'])
			dien['bigadd']=str(dien['JOB_ADDR_NO_DESCRIPT'][:3]).replace("'","").replace(";","").replace("{","")
			dien['smalladd']=str(dien['JOB_ADDR_NO_DESCRIPT'][3:]).replace("'","").replace(";","").replace("{","")

		return HRdata104


	finishArea=[]
	finishArea=[file.split(".")[0] for file in os.listdir(savedir+"/"+nowdate)] 


	#print("已完成項目",finishArea)
	#找大區域資料
	for bigkey in bigAreaList:
		area="60010%s000"%bigkey

		#判斷是否已有該區資料
		if area not in finishArea:
			URL2=URL+"&area=%s"%area
			res=requests.get(URL2)
			time.sleep(1.5)

			#判斷是否連上
			if res.status_code==200:
				data=None
				while data==None:
					try:
						res=requests.get(URL2)
						data=json.loads(res.text)
					except:
						time.sleep(15)
				
				allpage=int(data["TOTALPAGE"])

				#判斷是否有該頁資料
				if allpage!=0:

					#判斷資料是否小於三千 是的話抓大區資料(104一次只能顯示20頁(3000筆) 多的不給抓)
					if allpage<21:
						HRdata104=get104JsonData(allpage,URL2)
						with open(savedir+"/"+nowdate+"/"+area+".json","w") as f:
							json.dump(HRdata104,f)
						#print(area)
					#如果資料大於三千，則抓小區域資料
					else:
						for smallkey in samllAreaList:
							area="60010%s0%s"%(bigkey,smallkey)
							if area not in finishArea:
								URL2=URL+"&area=%s"%area
								res=requests.get(URL2)
								time.sleep(1)
								if res.status_code==200:
									data=json.loads(res.text)
									allpage=int(data["TOTALPAGE"])
									if allpage!=0:
										HRdata104=get104JsonData(allpage,URL2)
										with open(savedir+"/"+nowdate+"/"+area+".json","w") as f:
											json.dump(HRdata104,f)
										#print(area)



	savedir="../data/104json"+"/"+nowdate
	finishArea=[file.split(".")[0] for file in os.listdir(savedir)]
	datalist=[json.load(open(savedir+"/"+file)) for file in os.listdir(savedir)]
	def flat_list_v_1(the_list):
		is_nested = True
		before = the_list[:]
		while is_nested:
			is_nested = False
			now = []
			for item in before:
				if isinstance(item, list):
					now.extend(item)
					is_nested = True
				else:
					now.append(item)
			before = now
		return before
	alldata=flat_list_v_1(datalist)




	import pymongo
	from pymongo import MongoClient
	import datetime
	# import json
	# import time
	# from functools import reduce
	#連Mongodb
	client = MongoClient('localhost', 27017,username='j122085',password='850605')
	#連DB名
	db=client['rawData']
	#秀DB內的collection list
	db.collection_names()
	#選擇我們想要的collection
	collection = db.HRdata104
	# collection.drop()
	# collection.insert_many(alldata)


	e=time.time()
	#print(e-b)
	#print("已爬取完畢")
	#==================================================
	from sklearn.feature_extraction.text import CountVectorizer
	from sklearn.feature_extraction.text import TfidfTransformer
	from sklearn import svm
	import gc
	import time
	import jieba

	stopwordset = set()
	with open(r'stopwords.txt', 'r',encoding="big5") as sw:
		for line in sw:
			stopwordset.add(line.strip('\n'))
			

	def cut_text_list(textlist):
		textcutlist=[]
		words=["餐飲","餐廳","集團","小舖","飯店","股份","系統","國際","50嵐",'和牛','鐵板燒',"商務","埼玉","拉麵","會社","早午餐"]
		
		for word in words:    
			jieba.add_word(word)
			
		newstopwords=["有限公司",'股份','集團',"服務","安心","分公司",'企業',
					 '_',"台灣","股份","管理","顧問","店","系統","台北","國際",
					 "商行","法人","基金","文化","商務","工業","公司","醫院","管理","實業","人才","基金","文教"]
		for stopword in newstopwords:
			stopwordset.add(stopword)   
		for text in textlist:
			cutwords=jieba.cut(text)
			cuttext=" ".join([word for word in cutwords if word not in stopwordset and '\u4e00' <= word <= '\u9fff'])
			textcutlist.append(cuttext)
		return textcutlist

	#print("分詞ipeen")
	collectionIpeen=db.ipeenInfo
	ipeenData=list(collectionIpeen.find())
	dienName=list([work['name'].split("(")[0] for work in ipeenData])
	bigStyleList=list([work['bigstyle'].split("(")[0] for work in ipeenData])
	smallStyleList=list([work['smallstyle'].split("(")[0] for work in ipeenData])
	pincutlist=cut_text_list(dienName)

	count_vect=CountVectorizer()
	X_train_counts=count_vect.fit_transform(pincutlist)

	tfidf_transformer=TfidfTransformer()
	X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
	gc.collect()

	#print("分詞104")
	collectionHR=db.HRdata104
	HRdata=alldata
	# HRdata=list(collectionHR.find({}))
	name=list([work['NAME'] for work in HRdata])
	hr=list([work['NAME']+" "+work['PRODUCT'] for work in HRdata])
	docs_new=cut_text_list(hr)
	X_new_counts= count_vect.transform(docs_new)
	x_new_tfidf=tfidf_transformer.transform(X_new_counts)

	gc.collect()

	e=time.time()
	#print(e-b)
	#print("已分詞完畢")


	#print("開始svm訓練")
	#試用svm分群
	# from sklearn import svm
	st=time.time()
	clfbigStyle = svm.SVC(kernel="linear").fit(X_train_tfidf,bigStyleList)

	#print("svm預測")
	predictedBigStyle =clfbigStyle.predict(x_new_tfidf)
	#print(predictedBigStyle)
	ed=time.time()
	from collections import Counter
	Counter(predictedBigStyle)

	gc.collect()

	e=time.time()
	#print(e-b)
	#print("已預測完畢")

	for work,bigstyle in zip(HRdata,list(predictedBigStyle)):
		work['bigstyle']=bigstyle


	# ids=[data.pop("_id") for data in datas]
	# operations=[UpdateOne({"_id":idn},{'$set':data},upsert=True) for idn ,data in zip(ids,datas)]
	# collectionInfo.bulk_write(operations)

	collectionHR.drop()
	collectionHR.insert_many(HRdata)
	NData=collectionHR.count()
	#==================================================

	#把不要的json檔案刪除
	command = "rm -rf %s"
	command = command % savedir
	result = os.system(command)
	if result == 0:
		print ("刪除檔案成功")
	else:
		print ("刪除檔案沒成功")


	# HRdata104=list(collectionHR.find({}))
	# client.close()

	# #print("讀取完畢")
	# [i.pop("_id") for i in HRdata104]
	# import pandas as pd
	# df = pd.DataFrame(HRdata104)
	# writer = pd.ExcelWriter('../data/104_'+nowdate+'.xlsx', engine='xlsxwriter')
	# df.to_excel(writer, sheet_name='Sheet1')
	# writer.save()
	# #print("儲存完畢")

	e=time.time()

	msg = EmailMessage()
	msg.set_content("\n".join([str(time.strftime("%Y/%m/%d %H:%M")),
							   "Cost {} second".format(round(e-b)),
							   "We crawled {} datas".format(NData)]))
	msg['Subject'] = 'The Hr Crawler is finished'
	msg['From'] = "ServerNet"
	msg['To'] = 'andy.yuan@wowprime.com'
	with smtplib.SMTP('192.168.2.1',25) as s:
		s.send_message(msg)
except Exception as e:
	msg = EmailMessage()
	msg.set_content("104Crawler "+str(e)+str(sys.exc_info()[2].tb_lineno))
	msg['Subject'] = 'The 104 Crawler has some error'
	msg['From'] = "ServerNet"
	msg['To'] = 'andy.yuan@wowprime.com'
	with smtplib.SMTP('192.168.2.1',25) as s:
		s.send_message(msg)
