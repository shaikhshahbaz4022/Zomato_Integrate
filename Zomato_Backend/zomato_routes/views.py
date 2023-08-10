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


def UpdateData(req):
    if req.method == "PATCH":
        body = json.loads(req.body)
        id = body['id']
        for item in array:
            if item['id'] == id:
                item['available'] = 'yes'
            else:
                return HttpResponse(json.dumps({"msg": "Item is Not Present"}))
    else:
        return HttpResponse(json.dumps({"msg": "Invalid Request"}))
    return HttpResponse(json.dumps({"msg": "Item Updated Succesfully"}))


def DeleteData(req):
    if req.method == "DELETE":
        body = json.loads(req.body)
        id = body['id']
        for item in array:
            if item['id'] == id:
                array.remove(item)
            else:
                return HttpResponse(json.dumps({"msg": "Item is Not Present"}))
    else:
        return HttpResponse(json.dumps({"msg": "Invalid Request"}))
    return HttpResponse(json.dumps({"msg": "Item Deleted Succesfully"}))
