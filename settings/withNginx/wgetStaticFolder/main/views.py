
import os
import hashlib
import time
import subprocess
from django.shortcuts import render
from django.http import HttpResponse

def _get_md5(key):
    return hashlib.md5(key.encode()).hexdigest()

def _run_wget(foldername):
    path = f"/var/www/html/{foldername}/"
    os.mkdir(path)
    res = subprocess.run(
        ["wget", "-r", "-nH", "--no-parent", "www.example.com", "-P", path], 
        capture_output=True,
        text=True)

def hello(request):
    ts = str(time.time())
    _run_wget(_get_md5(ts))

    return HttpResponse("hello")



