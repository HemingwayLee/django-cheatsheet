import os
import traceback
import json
import string
import random
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import MyKey
from .myaes import AESCipher


@require_http_methods(["GET"])
def hello(request):
    keys = serializers.serialize(
        'json', 
        MyKey.objects.all()
    )
    
    return render(request, "dashboard.html", {
        "PAGEID": "dashboard",
        "KEYS": keys
    })

@require_http_methods(["POST"])
def insert(request):
    try:
        data = request.body.decode('utf-8') 
        received_json_data = json.loads(data) 

        mac = received_json_data['mac']
        username = received_json_data['username']
        pagecount = received_json_data['pagecount']
        expireddate = received_json_data['expireddate']
        
        # TODO: make it unique
        secret = ''.join(random.sample(string.ascii_lowercase, 16))
        aes = AESCipher(secret)
        license_key=aes.encrypt(data)

        aKey = MyKey(
            mac=mac, 
            name=username, 
            page_count_limit=pagecount, 
            expired_date=expireddate,
            secret=secret,
            license_key=license_key
        )
        aKey.save()

        return JsonResponse({"key": license_key})
    except:
        print(traceback.format_exc())
        return HttpResponse("server error", status=500)
    

@require_http_methods(["GET"])
def create(request):
    return render(request, "create.html", {
        "PAGEID": "create"
    })

@require_http_methods(["GET"])
def valid(request):
    return render(request, "valid.html", {
        "PAGEID": "valid"
    })

@require_http_methods(["POST"])
def do_validation(request):
    try:
        data = request.body.decode('utf-8') 
        received_json_data = json.loads(data) 

        akey = received_json_data['mykey']
        print(akey)
        theKey = MyKey.objects.filter(license_key=akey).first()
        
        print(theKey.secret)
        aes = AESCipher(theKey.secret)
        
        license_key=aes.decrypt(akey)
        print(license_key)
        
        return JsonResponse(json.loads(license_key), safe=False, status=200)
    except:
        print(traceback.format_exc())
        return HttpResponse(status=500)

# @require_http_methods(["POST"])
# def dosignin(request):
#     try:
#         user = authenticate(
#             username=request.POST["account"], 
#             password=request.POST["password"])
#         if not user:
#             return HttpResponse(status=404)

#         login(request, user)
#         return HttpResponse(status=200)
#     except:
#         print(traceback.format_exc())
#         return HttpResponse(status=500)

# @require_http_methods(["POST"])
# def signout(request):
#     logout(request)
#     return HttpResponse(status=200)

