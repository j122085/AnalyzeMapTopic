# from django.views.decorators.csrf import csrf_exempt
# import json
# from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse
import pymongo


# Create your views here.
# @csrf_exempt
def ipeen_list(request):
    print(request.POST)
    bigstyle = request.POST.get('bigstyle',"")
    bigadd = request.POST.get('bigadd', "")
    smalladd = request.POST.get('smalladd', "")

    queryElements={}
    if bigstyle != "":
        queryElements["bigstyle"] = bigstyle
    if bigadd != "":
        queryElements["bigadd"] = bigadd
    if smalladd != "":
        queryElements["smalladd"] = smalladd

    if bigstyle+bigadd+smalladd=="":
        return JsonResponse({"不行": "什麼都沒篩會有一堆值，不給你"}, safe=False)
    else:
        client = pymongo.mongo_client.MongoClient("localhost", 27017)
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
        client = pymongo.mongo_client.MongoClient("localhost", 27017)
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
        return JsonResponse(hr104data, safe=False)

# @csrf_exempt
def human_count_list(request):
    client = pymongo.mongo_client.MongoClient("localhost", 27017)
    collection = client.rawData.Nhuman
    Nhumnandata = list(collection.find({}))
    client.close()
    for dien in Nhumnandata:
        dien["weight"] = int(dien.pop("Nhuman"))/100
        dien["add"] = dien.pop("_id")
    return JsonResponse(Nhumnandata, safe=False)

# @csrf_exempt
def cost_power_list(request):
    client = pymongo.mongo_client.MongoClient("localhost", 27017)
    collection = client.rawData.CostPower
    CostPowerdata = list(collection.find({}))
    client.close()
    for dien in CostPowerdata:
        dien["weight"] = int(dien.pop('costPower'))
        dien["add"] = dien.pop("_id")
    return JsonResponse(CostPowerdata, safe=False)


def post_list(request):
    return render(request, 'api/ipeen_list.html', {})

def map(request):
    return render(request, 'api/map.html', {})


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


