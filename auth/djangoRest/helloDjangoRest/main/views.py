from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib import auth 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
import json

@api_view(["GET"])
def signout(request):
    auth.logout(request)
    return render(request, 'form_template.html')

@api_view(["GET"])
@permission_classes((AllowAny, ))
def signin(request):
    return render(request, 'form_template.html')

@api_view(["POST"])
@permission_classes((AllowAny, ))
def do_signin(request):
    body = json.loads(request.body.decode("utf-8"))
    print(body["username"])
    print(body["password"])

    user = auth.authenticate(username=body["username"], password=body["password"])

    if user is not None and user.is_active:
        print("Successful, return token")
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({"token": str(token)}, safe=False, status=200)
    else:
        print("user not exist... redirect to signin page...")
        return render(request, 'form_template.html')

@api_view(["GET"])
# @permission_classes((AllowAny, ))
def hello(request):
    # if request.user.is_authenticated: 
    #     return render(request, 'hello.html')
    # else:
    #     return render(request, 'form_template.html')
    return render(request, 'hello.html')
