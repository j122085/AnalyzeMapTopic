# from django.views.decorators.csrf import csrf_exempt
# import json
# from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse
import pymongo
from math import radians, cos, sin, asin, sqrt

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

# Create your views here.
# @csrf_exempt
def ipeen_list(request):
    print(request.POST)
    bigstyle = request.POST.get('bigstyle',"")
    smallstyle = request.POST.get('smallstyle', "")
    bigadd = request.POST.get('bigadd', "")
    smalladd = request.POST.get('smalladd', "")
    try:
        radius = int(request.POST.get('radius', ""))
        centerlat = float(request.POST.get('centerlat', ""))
        centerlng = float(request.POST.get('centerlng', ""))
    except:
        radius =""
        centerlat=""
        centerlng=""


    # print(radius,centerlat,centerlng)
    queryElements={}
    if bigstyle != "":
        queryElements["bigstyle"] = bigstyle
    if smallstyle != "":
        queryElements["bigstyle"] = smallstyle
    if bigadd != "":
        queryElements["bigadd"] = bigadd
    if smalladd != "":
        queryElements["smalladd"] = smalladd
    # if radius != "":
    #     queryElements["radius"] = radius

    if bigstyle+bigadd+smalladd=="":
        return JsonResponse({"不行": "什麼都沒篩會有一堆值，不給你"}, safe=False)
    else:
        client = pymongo.mongo_client.MongoClient("localhost", 27017,username='j122085',password='850605')
        # collection = client.rawData.wowprimeipeen
        collection = client.rawData.ipeenInfo
        ipeendata = list(collection.find(queryElements))
        client.close()
        ipeendata = [dien for dien in ipeendata if dien['status'] == "正常營業"
                                                 and dien['lat'] > 18
                                                 and dien['lat'] < 27
                                                 and dien['lng'] < 125
                                                 and dien['lng'] > 117
                                                 and dien['bigadd'] != 0
                                                 and dien['smalladd'] != 0]
        if radius != "":#lng1, lat1, lng2, lat2
            ipeendata=[dien for dien in ipeendata if haversine(lng1=dien["lng"], lat1=dien["lat"], lng2=centerlng, lat2=centerlat)<radius]

        for dien in ipeendata:
            dien["id"] = dien.pop("_id")
            # del dien["_id"]


        return JsonResponse(ipeendata, safe=False)



# @csrf_exempt
def hr104_list(request):
    print(request.POST)
    job = request.POST.get('job', "")
    bigadd = request.POST.get('bigadd', "")
    smalladd = request.POST.get('smalladd', "")
    bigstyle = request.POST.get('bigstyle', "")#0124
    try:
        radius = int(request.POST.get('radius', ""))
        centerlat = float(request.POST.get('centerlat', ""))
        centerlng = float(request.POST.get('centerlng', ""))
    except:
        radius =""
        centerlat=""
        centerlng=""

    queryElements = {}
    if job != "":
        queryElements["JOBCAT_DESCRIPT"] = job
    if bigadd != "":
        queryElements["bigadd"] = bigadd
    if smalladd != "":
        queryElements["smalladd"] = smalladd
    if bigstyle != "":#0124
        queryElements["bigstyle"] = bigstyle#0124
    # print(queryElements)

    if job + bigadd + smalladd + bigstyle == "":
        return JsonResponse({"不行": "什麼都沒篩會有一堆值，不給你"}, safe=False)
    else:
        client = pymongo.mongo_client.MongoClient("localhost", 27017,username='j122085',password='850605')
        collection = client.rawData.HRdata104
        hr104data = list(collection.find(queryElements))
        client.close()
        hr104data = [dien for dien in hr104data if dien['LAT'] > 18
                     and dien['LAT'] < 27
                     and dien['SAL_MONTH_LOW'] > 18000
                     and dien['SAL_MONTH_LOW'] < 100000
                     and dien['LON'] < 125
                     and dien['LON'] > 117
                     and dien['bigadd'] != 0
                     and dien['smalladd'] != 0]



        for dien in hr104data:
            dien["lat"] = dien.pop("LAT")
            dien["lng"] = dien.pop("LON")
            del dien["_id"]

        if radius != "":#lng1, lat1, lng2, lat2
            hr104data=[dien for dien in hr104data if haversine(lng1=dien["lng"], lat1=dien["lat"], lng2=centerlng, lat2=centerlat)<radius]


        return JsonResponse(hr104data, safe=False)

# @csrf_exempt
def human_count_list(request):

    try:
        radius = int(request.POST.get('radius', ""))
        centerlat = float(request.POST.get('centerlat', ""))
        centerlng = float(request.POST.get('centerlng', ""))
    except:
        radius =""
        centerlat=""
        centerlng=""

    client = pymongo.mongo_client.MongoClient("localhost", 27017,username='j122085',password='850605')
    collection = client.rawData.Nhuman
    Nhumandata = list(collection.find({}))
    client.close()
    for dien in Nhumandata:
        dien["weight"] = int(dien.pop("Nhuman"))
        dien["add"] = dien.pop("_id")

    if radius != "":  # lng1, lat1, lng2, lat2
        Nhumandata = [dien for dien in Nhumandata if haversine(lng1=dien["lng"], lat1=dien["lat"], lng2=centerlng, lat2=centerlat) < radius]

    return JsonResponse(Nhumandata, safe=False)

# @csrf_exempt
def cost_power_list(request):
    print(request.POST)
    try:
        radius = int(request.POST.get('radius', ""))
        centerlat = float(request.POST.get('centerlat', ""))
        centerlng = float(request.POST.get('centerlng', ""))
    except:
        radius =""
        centerlat=""
        centerlng=""

    client = pymongo.mongo_client.MongoClient("localhost", 27017,username='j122085',password='850605')
    collection = client.rawData.CostPower
    CostPowerdata = list(collection.find({}))
    client.close()
    for dien in CostPowerdata:
        dien["weight"] = int(dien.pop('costPower'))
        dien["add"] = dien.pop("_id")

    if radius != "":  # lng1, lat1, lng2, lat2
        CostPowerdata = [dien for dien in CostPowerdata if haversine(lng1=dien["lng"], lat1=dien["lat"], lng2=centerlng, lat2=centerlat) < radius]

    return JsonResponse(CostPowerdata, safe=False)


def post_list(request):
    return render(request, 'api/ipeen_list.html', {})

def Amap(request):
    # return render(request, 'api/map.html', {})
    return render(request, 'api/mapNew.html', {})

    # from .models import Ipeen
    # from .models import Hr104
    # if bigstyle!="":
    #     if smalladd!="":
    #         if bigadd!="":
    #             ipeendata = list(collection.find({"bigstyle": bigstyle, "bigadd":bigadd, "smalladd":smalladd}))
    #         else:
    #             ipeendata = list(collection.find({"bigstyle": bigstyle, "smalladd": smalladd}))
    #     elif bigadd!="":
    #         ipeendata = list(collection.find({"bigstyle": bigstyle, "bigadd": bigadd}))
    #     else:
    #         ipeendata = list(collection.find({"bigstyle": bigstyle}))
    # else:
    #     if smalladd!="":
    #         if bigadd=="":
    #             ipeendata = list(collection.find({"smalladd": smalladd}))
    #         else:
    #             ipeendata = list(collection.find({"bigadd": bigadd, "smalladd": smalladd}))
    #     elif bigadd!="":
    #         ipeendata = list(collection.find({"bigadd": bigadd}))
    #     else:
    #         return JsonResponse({"不行":"什麼都沒篩會有一堆值，不給你"},safe=False)

    #-----------------------
    # ipeendata = [dien for dien in ipeendata if dien['lat'] != 0 and dien['status'] == "正常營業"
    #              and dien['lat'] > 18 and dien['lat'] < 27 and dien['lng'] < 125 and dien['lng'] > 117]
    # import re
    # for dien in ipeendata:
    #     del dien["_id"]
    # #-----------------------
    # return JsonResponse(ipeendata, safe=False)
    # if bigstyle!="":
    #     if smalladd!="":
    #         if bigadd=="":
    #             dataIpeen = Ipeen.objects.filter(bigstyle=bigstyle,  smalladd=smalladd)
    #         else:
    #             dataIpeen = Ipeen.objects.filter(bigstyle=bigstyle, bigadd=bigadd, smalladd=smalladd)
    #     elif bigadd!="":
    #         dataIpeen = Ipeen.objects.filter(bigstyle=bigstyle, bigadd=bigadd)
    #     else:
    #         dataIpeen = Ipeen.objects.filter(bigstyle=bigstyle)
    # else:
    #     if smalladd!="":
    #         if bigadd=="":
    #             dataIpeen = Ipeen.objects.filter( smalladd=smalladd)
    #         else:
    #             dataIpeen = Ipeen.objects.filter(bigadd=bigadd, smalladd=smalladd)
    #     elif bigadd!="":
    #         dataIpeen = Ipeen.objects.filter(bigadd=bigadd)
    #     else:
    #         return JsonResponse({"RRR":"什麼都沒篩會有一堆值，不給你"},safe=False)

    # posts_serialized=serializers.serialize('json',dataIpeen)
    # return JsonResponse(posts_serialized, safe=False)



    # job = request.POST['job_descript']
    # job = request.POST.get('job_descript')
    # dataHr104 = Hr104.objects.filter(job_descript=job)
    # posts_serialized = serializers.serialize('json', dataHr104)
    # return JsonResponse(posts_serialized, safe=False)


