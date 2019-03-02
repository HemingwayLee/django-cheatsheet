from django.shortcuts import render
from django.http import HttpResponse
from .models import MyUser

def doSignup(request):
    MyUser.objects.create_user("abc@gmail.com", "1985-04-14", "test")

    return HttpResponse("created!", status=200)