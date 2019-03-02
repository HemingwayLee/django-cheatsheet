from django.shortcuts import render
from django.http import HttpResponse
from .models import MyUser

def doSignup(request):
    MyUser.objects.create_user("ywlee", "ywlee@gmail.com", "test")

    return HttpResponse("created!", status=200)