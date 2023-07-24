from django.http import HttpResponse
from . import task
import logging

logger = logging.getLogger(__name__)

def callme(request):
    task.demo_task('hello, bg')
    return HttpResponse("Hello, check your console")