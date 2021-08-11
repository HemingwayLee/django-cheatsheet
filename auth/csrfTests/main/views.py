import traceback
from django.shortcuts import render
from django.middleware.csrf import get_token
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
@login_required(login_url='/signin/')
def hello(request):
    return render(request, "hello.html")

@require_http_methods(["GET"])
def signin(request):
    return render(request, "signin.html")

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
def signout(request):
    logout(request)
    return HttpResponse(status=200)


@require_http_methods(["GET"])
def code(request):
    if request.GET.get('secret', False) == 'ELECTRON_APP':
        token = get_token(request)
        return JsonResponse({'token': token, 'success': 'true'})
    else:
        return JsonResponse({'error': 'true', 'msg': 'Invalid secret'}, status=403)


@require_http_methods(["GET"])
def code2(request):
    return render(request, "code2.html")


@require_http_methods(["GET"])
@login_required(login_url='/signin/')
def showposttemplate(request):
    return render(request, "post.html")


@require_http_methods(["GET"])
@login_required(login_url='/signin/')
def showpostmanually(request):
    return render(request, "post2.html")


@require_http_methods(["POST"])
def dopost1(request):
    print(request.POST)

    return JsonResponse({'success': 'true'})

