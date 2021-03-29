import os
import traceback
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
@login_required(login_url='/signin/')
def dashboard(request):
    return render(request, "dashbaord.html", {
        "ACCOUNTNAME": request.user,
        "PAGEID": "dashboard"
    })

@require_http_methods(["GET"])
@login_required(login_url='/signin/')
def account(request):
    return render(request, "account.html", {
        "ACCOUNTNAME": request.user,
        "PAGEID": "account"
    })

@require_http_methods(["GET"])
@login_required(login_url='/signin/')
def course(request):
    return render(request, "course.html", {
        "ACCOUNTNAME": request.user,
        "PAGEID": "course"
    })

@require_http_methods(["GET"])
@login_required(login_url='/signin/')
def visualization(request):
    return render(request, "visualization.html", {
        "ACCOUNTNAME": request.user,
        "PAGEID": "visualization"
    })

@require_http_methods(["GET"])
def signin(request):
    return render(request, "signin.html")

@require_http_methods(["POST"])
def dosignin(request):
    try:
        user = authenticate(
            username=request.POST["account"], 
            password=request.POST["password"])
        if not user:
            return HttpResponse(status=404)

        login(request, user)
        return HttpResponse(status=200)
    except:
        print(traceback.format_exc())
        return HttpResponse(status=500)

@require_http_methods(["POST"])
def signout(request):
    logout(request)
    return HttpResponse(status=200)

