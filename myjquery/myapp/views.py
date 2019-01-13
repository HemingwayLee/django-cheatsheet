import json
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def hello(request):
    return JsonResponse(json.loads('{"abc": 123}'), status=200)