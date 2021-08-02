import string
import random
import datetime
from background_task.models import Task
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from .task import uploadInBackground, doReport
from .models import MyTask, MyReport

def _id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@require_http_methods(["GET"])
def hello(request):
    return JsonResponse(list(MyTask.objects.values()), safe=False)


@require_http_methods(["GET"])
def check(request):
    return JsonResponse(list(MyReport.objects.values()), safe=False)


@require_http_methods(["GET"])
def task(request):
    status = 0
    filename = _id_generator()
    task = MyTask(filename=filename, status=status)
    task.save()
    uploadInBackground(filename)

    # Should be UTC
    target = datetime.datetime(year=2021, month=8, day=2, hour=1, minute=55)
    
    final = datetime.datetime(2500, 1, 1)
    # doReport(schedule=target, repeat=Task.DAILY, repeat_until=final)
    doReport(schedule=target, repeat=60, repeat_until=final)
    
    return HttpResponse('task is running, go to hello or check')

