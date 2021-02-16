import time
import random
from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    time.sleep(random.randint(0, 5))
    return HttpResponse("hello")

def hi(request):
    time.sleep(random.randint(2, 7))
    return HttpResponse("hello")

def hola(request):
    time.sleep(random.randint(4, 9))
    return HttpResponse("hola")


