from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth 
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
import json

# TODO: do we need this?
@api_view(["GET"])
@permission_classes((AllowAny, ))
def is_login(request):
    if request.user.is_authenticated():
        return JsonResponse({"msg": "okay"})
    else:
        return JsonResponse({"msg": "not auth"}, status=403)
    

@api_view(["GET"])
@permission_classes((AllowAny, ))
def hello(request):
    return render(request, 'hello.html', {
        'PAGE_URL': "/"
    })

@api_view(["GET"])
@permission_classes((AllowAny, ))
def handler404(request, exception):
    print(f"{request.path} 404, redirect...") 
    return render(request, 'hello.html', {
        'PAGE_URL': request.path
    })


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

        # Try to avoid AssertionError: The `request` argument must be an instance of `django.http.HttpRequest`, not `rest_framework.request.Request`
        print(f"inner method {request._request.method}")
        print(f"inner meta {request._request.META}")
        request._request.method = 'GET'
        request._request.META['Authorization'] = 'Token ' + str(token.key)
    else:
        print("user not exist...")

    return render(request, 'hello.html', {
        'PAGE_URL': "/"
    })


@api_view(["POST"])
def do_signout(request):
    auth.logout(request)
    
    return render(request, 'hello.html', {
        'PAGE_URL': "/"
    })

