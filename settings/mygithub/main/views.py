import os 
import json
import subprocess
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse

def hello(request):
    res = subprocess.run(
        ["git", "diff", "--no-index", f"{settings.MEDIA_ROOT}/aaa/", f"{settings.MEDIA_ROOT}/bbb/"], 
        # stdout=subprocess.DEVNULL, 
        # stderr=subprocess.STDOUT,
        capture_output=True,
        text=True)

    return render(request, 'hello.html', {
        "result": json.dumps(res.stdout) 
    })


