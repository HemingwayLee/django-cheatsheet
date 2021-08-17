from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def hello(request):
    return render(request, 'hello.html')

@require_http_methods(["GET"])
def show_get(request):
    print(request.headers)
    return JsonResponse({"msg": "get"})

@require_http_methods(["POST"])
def show_post(request):
    print(request.headers)
    return JsonResponse({"msg": "post"})
