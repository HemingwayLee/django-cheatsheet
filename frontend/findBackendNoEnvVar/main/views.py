import traceback
import json
import os
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def index(request):
    return render(request, 'index.html')

def hello(request):
    return JsonResponse(json.loads('{"abc": 123}'), status=200)

def hellopost(request):
    body = json.loads(request.body.decode("utf-8"))
    print(body)

    return JsonResponse(json.loads('[{"abc":123},{"xyz":567}]'), safe=False, status=200)
