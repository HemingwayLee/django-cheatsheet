from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.shortcuts import render
import base64

def hello(request):
    return HttpResponse("hello, request")

def integer(request, myid):
    return HttpResponse("Hello, my id is " + str(myid))

def multiple(request, myid, name):
    return HttpResponse("Hello, %s. my id is %s" % (name, str(myid)))

# we need to put 002 on url, but it will show 2 in response
def three(request, num):
    return HttpResponse("Hello, my num is %s" % str(num))

def return_img(request):
    with open(settings.MEDIA_ROOT + "/hello.jpg", "rb") as f:
        img = f.read()
    
    return HttpResponse(img, content_type="image/jpg")

def return_base64_img(request):
    res = {}
    with open(settings.MEDIA_ROOT + "/hello.jpg", "rb") as f:
        data = base64.b64encode(f.read()).decode()
    
    res["js"] = data
    return JsonResponse(res) 

def show_base64(request):
    return render(request, "show.html")
