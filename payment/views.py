import json
import time
import requests
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Transaction


@api_view(http_method_names=["POST", "GET"])
def pay(request: HttpRequest):
    body = request.body.decode()
    body = json.loads(body)

    if body.get("method") == "CheckPerformTransaction":
        app = body.get("params").get("account").get("appid")
        try:
            app = int(app)
        except:
            app = 0
        url = "https://astrontest.uz/mypage/api/userid.php"
        data = {"id": app}
        res = requests.post(url=url, json=data)
        if res.json().get("status") == "success":
            print("transaction checked")
            return Response({
                "result": {
                    "allow": True
                }
            })
        else:
            return Response({
                "error": {
                    "code": -31050,
                    "message": {
                        "en": "User not found",
                        "ru": "User not found",
                        "uz": "Foydalanuvchi topilmadi"
                    }
                }
            })
    if body.get("method") == "CreateTransaction":
        print(body)
        transaction = Transaction.objects.create(
            id=body.get("params").get("id"),
            appid=body.get("params").get("account").get("appid"),
            state="1"
        )
        print("transaction created")
        return Response({
            "result": {
                "create_time": body.get("params").get("time"),
                "transaction": body.get("params").get("id"),
                "state": 1
            }
        })
    if body.get("method") == "PerformTransaction":
        transaction = Transaction.objects.get(id=body.get("params").get("id"))
        transaction.state = "2"
        transaction.save()
        url = "https://astrontest.uz/mypage/api/payment.php"
        # 59340990
        appid = transaction.appid
        try:
            appid = int(appid)
        except:
            appid = appid
        data = {"id": appid}
        print(body)
        res = requests.post(url=url, json=data)
        print("to'landi")
        return Response({
            "result" : {
                "transaction" : body.get("params").get("id"),
                "perform_time" : int(time.time()),
                "state" : 2
            }
        })
    if body.get("method") == "CancelTransaction":
        print("bekor qilindi")
        return Response({
            "result" : {
                "transaction" : body.get("params").get("id"),
                "calcel_time" : int(time.time()),
                "state" : -2
            }
        })
