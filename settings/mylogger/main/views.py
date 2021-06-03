from django.shortcuts import render
from django.http import HttpResponse
import logging

print(__name__)

logger = logging.getLogger(__name__)

def hello(request):
    logger.info("this is the log I am putting")
    return HttpResponse("hello")