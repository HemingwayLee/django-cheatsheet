import time
import random
from django.shortcuts import render
from django.http import HttpResponse

def __dummy(num):
    sum = 0
    for i in range(num):
        sum += random.randint(0, 1000)

    return sum

def hello(request):
    sum = __dummy(random.randint(2000, 3000))
    return HttpResponse(f"hello, {sum}")

def hi(request):
    sum = __dummy(random.randint(2200, 3500))
    return HttpResponse(f"hi, {sum}")

def hola(request):
    sum = __dummy(random.randint(2400, 4000))
    return HttpResponse(f"hola, {sum}")


