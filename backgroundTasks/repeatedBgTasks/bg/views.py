from django.http import HttpResponse
from datetime import datetime, time, timedelta, timezone
from . import task
import logging
import math

logger = logging.getLogger(__name__)

def callme(request):
    task.demo_task('hello, bg')
    return HttpResponse("Check your console")


def callRepeat(request):
    task.the_init_task(repeat=10, repeat_until=None)
    return HttpResponse("Check your logs")


def callOnTime(reuqest):
    logger.info("call in the API")

    utc_now = datetime.now()
    last_moment_tonight = datetime.combine(utc_now, time.max)
    gmat_9_now = utc_now + timedelta(hours=9)
    seconds_2_midnight = math.floor((last_moment_tonight - gmat_9_now).total_seconds())
    hours_2_midnight = seconds_2_midnight / 60 / 60
    print(f"last moment tonight: {last_moment_tonight}")
    print(f"JST local time now: {gmat_9_now}")
    print(f"{seconds_2_midnight} seconds to midnight")
    print(f"{hours_2_midnight} hours to midnight")

    # run after 90 seconds
    # task.the_init_task(schedule=90) 
    
    # run at midnight
    task.the_init_task(schedule=seconds_2_midnight) 

    return HttpResponse(f"{seconds_2_midnight} seconds to midnight")
