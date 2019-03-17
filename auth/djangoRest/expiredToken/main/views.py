import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib import auth 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test

# @api_view(["GET"])
# def signout(request):
#     auth.logout(request)
#     return render(request, 'form_template.html')

@api_view(["GET"])
@permission_classes((AllowAny, ))
def signin(request):
    return render(request, 'signin.html')

@api_view(["POST"])
@permission_classes((AllowAny, ))
def do_signin(request):
    body = json.loads(request.body.decode("utf-8"))
    user = auth.authenticate(username=body["username"], password=body["password"])

    if user is not None and user.is_active:
        print("Successful, return token")
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse(
            { "token": str(token.key), "is_staff": user.is_staff, "is_superuser": user.is_superuser }, 
            safe=False, 
            status=200)
    else:
        return HttpResponse(status=401)


@api_view(["GET"])
def hello(request):
    return JsonResponse({"status":"hello"}, safe=False, status=200)

