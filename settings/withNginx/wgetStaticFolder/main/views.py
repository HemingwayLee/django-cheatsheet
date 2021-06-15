
import os
import hashlib
import traceback
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

    return HttpResponse("crawled")

def side_by_side(request):
    try:
        dirs = [os.path.basename(x[0]) for x in os.walk("/var/www/html/")]
        print(dirs)

        # make sure we have at least 2 folder crawled...
        # dirs[0] is /var/www/html/
        return render(
            request, 
            'side_by_side.html', 
            { "CURR": dirs[1], "PREV": dirs[2] }
        )
    except:
        print(traceback.format_exc())
        return HttpResponse(status=500)

