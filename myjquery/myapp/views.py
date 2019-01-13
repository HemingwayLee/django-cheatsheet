import json
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html', {"address": "127.0.0.1"})

def hello(request):
    return JsonResponse(json.loads('{"abc": 123}'), status=200)

def table(request):
    return JsonResponse(json.loads('[{"abc":123},{"abc":567}]'), safe=False, status=200)