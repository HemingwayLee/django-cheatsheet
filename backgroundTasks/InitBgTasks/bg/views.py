from django.http import HttpResponse
from . import task
import logging

logger = logging.getLogger(__name__)

def callme(request):
    task.demo_task('hello, bg')
    return HttpResponse("Check your console")


def callRepeat(request):
    task.the_init_task(repeat=10, repeat_until=None)
    return HttpResponse("Check your logs")