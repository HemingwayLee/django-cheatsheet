from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def handler404(request, exception):
    print(f"{request.path} 404, redirect...") 
    return render(request, 'hello.html', {
        'PAGE_URL': request.path
    })

def show(request):
    return render(request, 'hello.html', {
        'PAGE_URL': "/home"
    })
