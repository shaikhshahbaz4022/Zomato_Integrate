from django.shortcuts import render
import json
from django.http import HttpResponse
# Create your views here.
from . import views
order = []
sum = 0


def CreateOrder(req):
    if req.method == "POST":
        body = json.loads(req.body)

        order.append(body)
    else:
        return HttpResponse(json.dumps({"msg": "Wrong Request"}))
    return HttpResponse(json.dumps({"msg": "Data Posted Succesfully"}))


def GetOrderData(req):
    if (req.method == "GET"):
        return HttpResponse(json.dumps({"data": order}))


def UpdateOrderStatus(req):
    if (req.method == "PATCH"):
        body = json.loads(req.body)
        id = body['id']
        status = body['status']
        for item in order:
            if item['id'] == id:
                item['status'] = status
            else:
                return HttpResponse(json.dumps({"msg": "ID Not Found"}))
    else:
        return HttpResponse(json.dumps({"msg": "Invalid Request"}))
    return HttpResponse(json.dumps({"msg": "Item Updated Succesfully"}))


def DeleteOrderStatus(req):
    if (req.method == "PATCH"):
        body = json.loads(req.body)
        id = body['id']
    
        for item in order:
            if item['id'] == id:

                order.remove(item)
            else:
                return HttpResponse(json.dumps({"msg": "ID Not Found"}))
    else:
        return HttpResponse(json.dumps({"msg": "Invalid Request"}))
    return HttpResponse(json.dumps({"msg": "Item Deleted Succesfully"}))
