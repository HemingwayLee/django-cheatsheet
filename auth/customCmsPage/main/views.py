from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import auth 

@require_http_methods(["GET"])
def signout(request):
    auth.logout(request)
    return HttpResponse("logout successfully")

# @login_required
def dashboard(request):
    if not request.user.is_authenticated: 
        print("Please login!!")
        return HttpResponseRedirect('login/')

    mail = request.user.username
    return HttpResponse("Hello, " + mail)
