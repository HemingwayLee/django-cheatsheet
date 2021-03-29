import os
import traceback
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.admin.views.decorators import staff_member_required


@require_http_methods(["GET"])
@login_required(login_url='/signin/')
def index(request):
    if request.user.is_staff:
        return redirect('/myadmin/')
    else:
        return redirect('/client/')

@require_http_methods(["GET"])
@login_required(login_url='/signin/')
@staff_member_required(login_url='/notfound/')
def myadmin(request):
    return render(request, "admin.html", {
        "ACCOUNTNAME": request.user,
        "PAGEID": "admin"
    })

@require_http_methods(["GET"])
@login_required(login_url='/signin/')
def client(request):
    return render(request, "client.html", {
        "ACCOUNTNAME": request.user,
        "PAGEID": "client"
    })

@require_http_methods(["GET"])
@login_required(login_url='/signin/')
@staff_member_required(login_url='/notfound/')
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

@require_http_methods(["GET"])
def notfound(request):
    logout(request)
    return render(request, "404.html")
