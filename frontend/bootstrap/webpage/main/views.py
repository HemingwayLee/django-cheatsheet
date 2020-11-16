import traceback
import json
import os
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponse

def index(request):
    return render(request, 'index.html')
