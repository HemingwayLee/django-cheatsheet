import traceback
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
@login_required(login_url='/page/signin/')
def dashboard(request):
    print("dashboard")
    return render(
        request, 
        'base.html', 
        { "ACCOUNTNAME": request.user, "PAGEID": "dashboard.html" }
    )

@require_http_methods(["GET"])
@login_required(login_url='/page/signin/')
def clients(request):
    return render(
        request, 
        'base.html', 
        { "ACCOUNTNAME": request.user, "PAGEID": "clients.html" }
    )

@require_http_methods(["GET"])
def signin(request):
    return render(
        request, 
        "base.html",
        { "ACCOUNTNAME": request.user, "PAGEID": "signin.html" }
    )

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
    try:
        logout(request)
        return HttpResponse(status=200)
    except:
        print(traceback.format_exc())
        return HttpResponse(status=500)
