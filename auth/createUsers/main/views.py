import traceback
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def hello(request):
    return render(request, "index.html")

# TODO:
# Forbidden (CSRF token missing or incorrect.)
# https://stackoverflow.com/questions/26639169/csrf-failed-csrf-token-missing-or-incorrect
@require_http_methods(["POST"])
def dosignin(request):
    try:
        user = authenticate(username=request.POST["account"], password=request.POST["password"])
        if not user:
            return HttpResponse(status=404)

        login(request, user)
        return HttpResponse(status=200)
    except:
        print(traceback.format_exc())
        return HttpResponse(status=500)


@require_http_methods(["POST"])
def dosignout(request):
    logout(request)
    return HttpResponse(status=200)

