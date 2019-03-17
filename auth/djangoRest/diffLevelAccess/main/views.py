import json
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import auth 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test

@api_view(["GET"])
def signout(request):
    request.user.auth_token.delete()
    return JsonResponse({"status":"signout"}, safe=False, status=200)

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
        return JsonResponse({"status":"account or password incorrect"}, safe=False, status=401)

@api_view(["GET"])
@permission_classes((AllowAny, ))
def nologin(request):
    return JsonResponse({"status":"everybody can see"}, safe=False, status=200)

@api_view(["GET"])
def login(request):
    return JsonResponse({"status":"login can see"}, safe=False, status=200)

@api_view(["GET"])
@staff_member_required
def staff(request):
    return JsonResponse({"status":"staff can see"}, safe=False, status=200)

@api_view(["GET"])
@user_passes_test(lambda u: u.is_superuser)
def superuser(request):
    return JsonResponse({"status":"super user can see"}, safe=False, status=200)


