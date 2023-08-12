from django.http import HttpResponse
from . import task

def callme(request):
    task.demo_task('hello, bg')
    return HttpResponse("Hello, check your console")