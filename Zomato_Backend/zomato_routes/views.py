from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
# Create your views here.
array = []


def Create(req):
    if req.method == "POST":
        body = json.loads(req.body)
        array.append(body)
        print(array)
    else:
        return HttpResponse(json.dumps({"msg": "Wrong Request"}))
    return HttpResponse(json.dumps({"msg": "Data Posted Succesfully"}))


def GetData(req):
    if (req.method == "GET"):
        return HttpResponse(json.dumps({"data": array}))
