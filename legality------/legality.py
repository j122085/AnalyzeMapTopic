# from requests import post
# from re import findall
# from json import loads
# from pyproj import Proj, transform
# from twd97 import towgs84
# from geocoder import google
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from time import sleep
# from pandas import read_excel
#
#
#
#
# def getComment(street,address,use,brand,layer):
#     def getCookie():
#         options = Options()
#         # options.add_argument("--headless")
#         options.add_argument("--no-sandbox")
#         options.add_argument("start-maximized")
#         options.add_argument("disable-infobars")
#         options.add_argument("--disable-extensions")
#
#         driver = webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=options)
#         driver.get("http://luz.tcd.gov.tw/web/")
#         sleep(2)
#         cookie=driver.get_cookies()[0]
#         sleep(0.5)
#         driver.quit()
#         with open(r"../api/legalityData/cookies.txt",'w') as f:
#             f.write(cookie['name']+"="+cookie['value'])
#         return cookie['name']+"="+cookie['value']
#
#     def taipei(areaClass, area=150, floorList=[1], use="餐飲"):
#         ter = 0
#         if "特" in areaClass:
#             print(areaClass, "需人工判斷該區為什麼區!-{}".format(address))
#             areaClass = input(
#                 "請人工查詢下方網頁(用門牌號碼>選區、路、巷弄號搜索，確認該區右方括弧內叫做什麼)\nhttps://www.zone.gov.taipei/new_showmapMain.aspx?noshow=0\n請輸入該區右方括弧內名稱:")
#             ter = 1
#         if "商" in areaClass:
#             if use != '餐飲' and area >= 300:
#                 judgment = "初評通過,但須檢討停車代金,請開發組進行品牌配對"
#             else:
#                 judgment = "初評通過,請開發組進行品牌配對"
#
#         elif "住" in areaClass:
#             if "住一" in areaClass or "住1" in areaClass or "第一種住" in areaClass or "第1種住" in areaClass:
#                 judgment = "初評不通過"
#             elif area < 150 and len([i for i in floorList if i in [1, -1]]) > 0:
#                 judgment = "初評通過,請開發組進行品牌配對(面臨道路寬需8公尺以上)"
#             elif areaClass in ["三之一", "三之二", "四之一", "3-1", "3-2", "4-1", "3之1", "3之2", "4之1"] and area < 500 and len(
#                     [i for i in floorList if i in [2, 1, -1]]) > 0:
#                 judgment = "初評通過,請開發組進行品牌配對(面臨道路寬需12公尺以上)"
#             elif len([i for i in floorList if i in [2, 1, -1]]) > 0:
#                 judgment = "初評通過,請開發組進行品牌配對(面臨道路寬需12公尺以上,使用面積大於規定500㎡>需判斷是否可分戶使用)"
#             else:
#                 judgment = "初評不通過"
#
#         elif "工" in areaClass:
#             if len([i for i in floorList if i in [2, 1, -1]]) > 0 and area < 300:
#                 judgment = "初評通過,請開發組進行品牌配對(同棟建築餐飲業+飲食業使用面積需在500㎡以下)"
#             elif len([i for i in floorList if i in [2, 1, -1]]) > 0 and area < 500:
#                 judgment = "初評通過,請開發組進行品牌配對(同棟建築餐飲業+飲食業使用面積需在500㎡以下,使用面積大於規定300㎡>需判斷是否可分戶使用)"
#             else:
#                 judgment = "初評不通過"
#
#         else:
#             judgment = "初評通過,請開發組進行品牌配對(須請建築師判斷)"
#         if ter == 0:
#             return judgment
#         elif ter == 1:
#             return judgment, areaClass
#
#     def taichung(areaClass,area=150,floorList=[1],use="餐飲"):
#         if "商" in areaClass:
#             if use!='餐飲' and area>=300:
#                 judgment="初評通過,但須檢討停車代金,請開發組進行品牌配對"
#             else:
#                 judgment="初評通過,請開發組進行品牌配對"
#         elif "住" in areaClass:
#             if "B種" in areaClass:
#                 judgment="初評不通過"
#             elif area<500:
#                 judgment="初評通過,請開發組進行品牌配對"
#             elif area>=500:
#                 judgment="初評通過,請開發組進行品牌配對(使用面積大於規定500㎡,需判斷是否可分戶使用)"
#         else:
#             judgment="初評通過,請開發組進行品牌配對(須請建築師判斷)"
#         return judgment
#
#
#     def Kaohsiung(areaClass, area=150, floorList=[1], use="餐飲"):
#         if "商" in areaClass:
#             if use != '餐飲' and area >= 300:
#                 judgment = "初評通過,但須檢討停車代金,請開發組進行品牌配對"
#             else:
#                 judgment = "初評通過,請開發組進行品牌配對"
#
#         elif "住" in areaClass:
#             if area < 300:
#                 if len([i for i in floorList if i in [1, -1]]) > 0:
#                     judgment = "初評通過,請開發組進行品牌配對"
#                 elif 2 in floorList:
#                     judgment = "路寬十五公尺以上初評通過,請開發組進行品牌配對"
#             elif len([i for i in floorList if i in [2, 1, -1]]) > 0:
#                 judgment = "初評通過,請開發組進行品牌配對(使用面積大於規定300㎡,需判斷是否可分戶使用)"
#             else:
#                 judgment = "初評不通過"
#         else:
#             judgment = "初評通過,請開發組進行品牌配對(須請建築師判斷)"
#         return judgment
#
#     def otherCity(areaClass,area,floorList=[1],use="餐飲"):
#         if "商" in areaClass:
#             if use!='餐飲' and area>=300:
#                 judgment="初評通過,但須檢討停車代金,請開發組進行品牌配對"
#             else:
#                 judgment="初評通過,請開發組進行品牌配對"
#         elif "住" in areaClass:
#             if area<300:
#                 judgment="初評通過,請開發組進行品牌配對"
#             elif area>=300:
#                 judgment="初評通過,請開發組進行品牌配對(使用面積大於規定300㎡,需判斷是否可分戶使用)"
#         else:
#             judgment="初評通過,請開發組進行品牌配對(須請建築師判斷)"
#         return judgment
#
#     # len([i for i in floorList if i in [2,1,-1]])>0:
#
#     def getDienMin():
#         dienMinDict = read_excel(r"../api/legalityData/dienMin.xlsx")
#         dienMinDict = dienMinDict.to_dict()
#         smallestDict = {i:[j for j in dienMinDict[i].values() if type(j)==str] for i in dienMinDict}
#         smallestDict = {j: i for i in smallestDict for j in smallestDict[i]}
#         return smallestDict
#
#
#     #######################################################################################go
#     dienList = {"2": "原燒",
#                 "3": "王品",
#                 "4": "聚",
#                 "5": "藝奇",
#                 "6": "夏慕尼",
#                 "7": "西堤",
#                 "8": "陶板屋",
#                 "10": "品田",
#                 "12": "石二鍋",
#                 "13": "舒果",
#                 "15": "hot7",
#                 "151": "禾樂",
#                 "16": "ita",
#                 "17": "莆田",
#                 "18": "酷必",
#                 "19": "麻佬大",
#                 "20": "乍牛",
#                 "22": "沐越",
#                 "23": "青花驕",
#                 "24": "享鴨",
#                 "25": "丰和日麗"}
#     smallestDict=getDienMin()
#
#     # dienType = input("是否為街邊店\n選項\n\t1:是\n\t2:否\n\t：")
#     street="1"
#     dienType = street
#     if dienType == "1":
#         dienType = '街邊'
#     elif dienType == "2":
#         dienType = '商場'
#
#     if dienType == '商場':
#         address = input("請輸入商場名稱、位置\n(例:中原家樂福-桃園市中壢區中華路二段501號):")
#         use = input("是否由商場辦理合法性?\n選項\n\t1:是\n\t2:否\n\t：")
#     elif dienType == '街邊':
#         # address = input("請輸入地址(須包含[市|縣]及[區|市|鎮|鄉]):")
#         address = address
#         #############################
#         # nF = int(input("共承租幾層?"))
#         nF = len(layer)
#         # layerData = {}
#         # for i in range(1, nF + 1):
#         #     nLayer = int(input("請輸入第{}筆承租樓層\n選項\n\t 1:一樓\n\t 2:二樓\n\t-1:地下一樓\n\t-2:地下二樓 (以此類推)\n\t:".format(i)))
#         #     nArea = float(input("請輸入使用面積(平方公尺)"))
#         #     layerData[nLayer] = nArea
#         # area = round(sum([layerData[i] for i in layerData]), 3)
#         # floorList = [i for i in layerData]
#         # print("總面積共{}平方公尺".format(area))
#         # #############################
#         # #     area=float(input("請輸入使用面積(平方公尺):"))
#         # #     floor=int(input("請輸入樓層\n選項\n\t 1:一樓\n\t 2:二樓\n\t-1:地下一樓\n\t-2:地下二樓\n\t:"))
#         # use = input("用途\n選項\n\t1:餐廳或飲食店\n\t2:其他-非餐飲\n\t：")
#         # if use == "1":
#         #     use = '餐廳或飲食店'
#         # elif use == "2":
#         #     use = '其他-非餐飲'
#         #
#         # brand = input("""品牌\n選項
#         #  2: '原燒',
#         #  3: '王品',
#         #  4: '聚',
#         #  5: '藝奇',
#         #  6: '夏慕尼',
#         #  7: 'ＴＡＳＴｙ',
#         #  8: '陶板屋',
#         #  10: '品田牧場',
#         #  12: '石二鍋',
#         #  13: '舒果',
#         #  15: 'hot 7',
#         #  151:'禾樂',
#         #  16: 'ita義塔',
#         #  17: '莆田',
#         #  18: 'CooK BEEF!',
#         #  19: '麻佬大',
#         #  20: '乍牛',
#         #  22: '沐越',
#         #  23: '青花驕',
#         #  24: '享鴨',
#         #  25: '丰和日麗'\n\t:""")
#         # brand = dienList[brand]
#         # smallest = smallestDict[brand]
#         # ##########################
#         # bigadd = ""
#         # smalladd = ""
#
#         try:
#             bigadd = findall("(..[市|縣])(\w\w?\w?[區|市|鎮|鄉])", address)[0][0]
#             smalladd = findall("(..[市|縣])(\w\w?\w?[區|市|鎮|鄉])", address)[0][1]
#         except:
#             pass
#         try:
#             road = address.split(smalladd)[1].split("、")[0]
#         except:
#             road = address.split("、")[0]
#             print("沒有市或區的地址，可能會不準確")
#
#         headersStr = """Accept: */*
#         Accept-Encoding: gzip, deflate
#         Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
#         Connection: keep-alive
#         Content-Length: 114
#         Content-Type: application/x-www-form-urlencoded; charset=UTF-8
#         Cookie: ASP.NET_SessionId=zyh3tb3y1zfoxairu3hr0mth
#         Host: luz.tcd.gov.tw
#         Origin: http://luz.tcd.gov.tw
#         Referer: http://luz.tcd.gov.tw/WEB/
#         User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
#         X-Requested-With: XMLHttpRequest"""
#         headerDict = {i.split(": ")[0].strip(): i.split(": ")[1].strip() for i in headersStr.split("\n")}
#
#         with open(r"../api/legalityData/cookies.txt",'r') as f:
#             cookieStr=f.read()
#
#         headerDict['Cookie'] = cookieStr
#
#         dataDict = {}
#         dataDict["VAL1"] = road
#         if bigadd != "":
#             dataDict["COUNTY"] = bigadd
#             dataDict["TOWN"] = smalladd
#             try:
#                 findXYUrl = "http://luz.tcd.gov.tw/WEB/ws_data.ashx?CMD=GETADDRESS"
#                 res = post(findXYUrl, data=dataDict, headers=headerDict)
#                 locationData = loads(res.text)
#             except:
#                 getCookie()
#                 with open(r"../api/legalityData/cookies.txt", 'r') as f:
#                     cookieStr = f.read()
#                 headerDict['Cookie'] = cookieStr
#                 res = post(findXYUrl, data=dataDict, headers=headerDict)
#                 locationData = loads(res.text)
#                 # return "資料讀取中，請等30秒後再來"
#
#
#             lat, lng = towgs84(locationData['AddressList'][0]['X'], locationData['AddressList'][0]['Y'])
#         else:
#             lat, lng = google(address).latlng
#             print(lat, lng)
#
#         P4326 = Proj(init='epsg:4326')
#         P3857 = Proj(init='epsg:3857')
#         x, y = transform(P4326, P3857, lng, lat)
#
#         queryHeadersStr = """Accept: */*
#         Accept-Encoding: gzip, deflate
#         Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
#         Connection: keep-alive
#         Content-Length: 69
#         Content-Type: application/x-www-form-urlencoded; charset=UTF-8
#         Cookie: ASP.NET_SessionId=zyh3tb3y1zfoxairu3hr0mth
#         Host: luz.tcd.gov.tw
#         Origin: http://luz.tcd.gov.tw
#         Referer: http://luz.tcd.gov.tw/WEB/
#         User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
#         X-Requested-With: XMLHttpRequest"""
#
#
#         queryHeaderDict = {i.split(": ")[0].strip(): i.split(": ")[1].strip() for i in queryHeadersStr.split("\n")}
#         queryHeaderDict['Cookie'] =cookieStr
#
#         queryData = {}
#         queryData["X"], queryData["Y"] = x, y
#         # queryData["X"],queryData["Y"]=13495533.107782178,2870575.0923182988
#
#         queryData["LAYERS"] = "5,3,6"
#         queryData['LANDLAYERS'] = ""
#         queryUrl = "http://luz.tcd.gov.tw/WEB/ws_identify.ashx"
#         res = post(queryUrl, data=queryData, headers=queryHeaderDict)
#         info = loads(res.text)
#         areaClass = info['5']['features'][0]['attributes']['使用分區']
#         print(areaClass)
#
#
#
#         #############################################################################################################
#         # nF = int(input("共承租幾層?")
#         # layerData = {}
#         # for i in range(1, nF + 1):
#         #     # nLayer = int(input("請輸入第{}筆承租樓層\n選項\n\t 1:一樓\n\t 2:二樓\n\t-1:地下一樓\n\t-2:地下二樓 (以此類推)\n\t:".format(i)))
#         #
#         #     nArea = float(input("請輸入使用面積(平方公尺)"))
#         #     layerData[nLayer] = nArea
#         layerData=layer
#
#         area = round(sum([layerData[i] for i in layerData]), 3)
#         floorList = [i for i in layerData]
#         print("總面積共{}平方公尺".format(area))
#         #############################
#         #     area=float(input("請輸入使用面積(平方公尺):"))
#         #     floor=int(input("請輸入樓層\n選項\n\t 1:一樓\n\t 2:二樓\n\t-1:地下一樓\n\t-2:地下二樓\n\t:"))
#         # use = input("用途\n選項\n\t1:餐廳或飲食店\n\t2:其他-非餐飲\n\t："
#         use=use
#         if use == "1":
#             use = '餐廳或飲食店'
#         elif use == "2":
#             use = '其他-非餐飲'
#
#         # brand = input("""品牌\n選項
#         #          2: '原燒',
#         #          3: '王品',
#         #          4: '聚',
#         #          5: '藝奇',
#         #          6: '夏慕尼',
#         #          7: 'ＴＡＳＴｙ',
#         #          8: '陶板屋',
#         #          10: '品田牧場',
#         #          12: '石二鍋',
#         #          13: '舒果',
#         #          15: 'hot 7',
#         #          151:'禾樂',
#         #          16: 'ita義塔',
#         #          17: '莆田',
#         #          18: 'CooK BEEF!',
#         #          19: '麻佬大',
#         #          20: '乍牛',
#         #          22: '沐越',
#         #          23: '青花驕',
#         #          24: '享鴨',
#         #          25: '丰和日麗'\n\t:""")
#         brand=brand
#         brand = dienList[brand]
#         smallest = smallestDict[brand]
#         ##########################
#         bigadd = ""
#         smalladd = ""
#         ##############################################################################################################
#         if dienType == '商場':
#             if use == "1":
#                 use = "商場會辦理合法性"
#                 judgment = "初評通過"
#             else:
#                 use = "但須由我方自行辦理合法業務"
#                 judgment = "初評通過(須請建築師判斷)"
#             print("本評估新點({})為商場店,{}。\n\n\t本案判斷:{}".format(address, use, judgment))
#         #     address=input("請輸入商場名稱、位置\n(例:中原家樂福-桃園市中壢區中華路二段501號):")
#         #     use=input("是否為商場辦理合法性?\n選項\n\t1:是\n\t2:否\n\t：")
#         else:
#
#             if smallest > area:
#                 judgment = "初評不通過,未達'{}'最小合法面積限制{}m2".format(brand, smallest)
#             elif bigadd == "台北市" or bigadd == "臺北市":
#                 if "特" in areaClass:
#                     judgment, areaClass = taipei(areaClass, area, floorList, use)
#                 else:
#                     judgment = taipei(areaClass, area, floorList, use)
#
#             elif bigadd == "台中市" or bigadd == "臺中市":
#                 judgment = taichung(areaClass, area, floorList, use)
#             elif bigadd == "高雄市":
#                 judgment = Kaohsiung(areaClass, area, floorList, use)
#             else:
#                 judgment = otherCity(areaClass, area, floorList, use)
#             layer_area = "、".join(
#                 ["{}F:{}㎡".format(i, layerData[i]) if i > 0 else "B{}:{}㎡".format(-i, layerData[i]) for i in layerData])
#             if nF == 1:
#                 return "================================\n本評估新點({})的使用分區為 {}，\n(建物面積：{}，用途：{})。\n\n\t本案判斷:{}-{}".format(
#                     address,
#                     areaClass, layer_area, use, brand, judgment)
#             else:
#                 return "================================\n本評估新點({})的使用分區為 {}，\n(建物面積：{}-共{}㎡，用途：{})。\n\n\t本案判斷:{}-{}".format(
#                         address,
#                         areaClass, layer_area, area, use, brand, judgment)
#
#
# if __name__=="__main__":
#     result=getComment(address="王品-台中市西區台灣大道二段218號",brand="2",street="1",use='1',layer={1:50,2:33,-1:53.6})
#     print(result)
#     # layer = {1: 50, 2: 33, -1: 53.6}
#     # layerData=layer
#     # area = round(sum([layerData[i] for i in layerData]), 3)
#     # print(area)