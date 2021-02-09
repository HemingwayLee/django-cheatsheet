from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth 
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
import json

@api_view(["GET"])
@login_required(login_url='/signin/')
def hello(request):
    return render(request, "hello.html")

@api_view(["GET"])
@permission_classes((AllowAny, ))
def signin(request):
    return render(request, 'form_template.html')

@api_view(["POST"])
@permission_classes((AllowAny, ))
def do_signin(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(username)
    print(password)

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        print("Successful, return token")
        token, _ = Token.objects.get_or_create(user=user)

        # Redirect does not work, because it only set header in response, not in the request...
        # response = redirect('/hello/')
        # response = HttpResponseRedirect('/hello/')
        # response['Authorization'] = 'Token ' + str(token.key)
        # return response
        
        # Try to avoid AssertionError: The `request` argument must be an instance of `django.http.HttpRequest`, not `rest_framework.request.Request`
        print(f"inner method {request._request.method}")
        print(f"inner meta {request._request.META}")
        request._request.method = 'GET'
        request._request.META['Authorization'] = 'Token ' + str(token.key)
        return hello(request._request)

        # Or maybe I can simply do this...
        # return render(request, "hello.html")
    else:
        print("user not exist...")
        return render(request, 'form_template.html')

@api_view(["GET"])
def signout(request):
    auth.logout(request)
    return render(request, 'form_template.html')

