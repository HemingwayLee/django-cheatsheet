
import os
import hashlib
import traceback
import time
import json
import subprocess
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pathlib import Path


def _get_md5(key):
    return hashlib.md5(key.encode()).hexdigest()

def _run_wget(foldername, url):
    path = f"/var/www/html/{_get_md5(url)}/{foldername}/"
    os.makedirs(path)
    res = subprocess.run(
        ["wget", "-r", "-nH", "--no-parent", f"'{url}'", "-P", path], 
        capture_output=True,
        text=True)

def crawl_url(request):
    try:
        body = json.loads(request.body.decode("utf-8"))
        url = body["url"]
        print(url)

        ts = str(time.time())
        _run_wget(ts, url)

        return JsonResponse({})
    except:
        print(traceback.format_exc())
        return HttpResponse(status=500)

def main(request):
    p = Path("/var/www/html/")

    res = []
    dirs = [f for f in p.iterdir() if f.is_dir()]
    for d in dirs:
        print(str(d))
        subPath = Path(d)
        res.append({str(d): [str(f.stem) for f in subPath.iterdir() if f.is_dir()]})

    return render(request, "index.html", {
        "DIRS": json.dumps(res)
    })

def side_by_side(request, hashcode):
    try:
        p = Path(f"/var/www/html/{hashcode}/")
        dirs = [str(f.stem) for f in p.iterdir() if f.is_dir()]

        if len(dirs) == 2:
            return render(
                request, 
                'side_by_side.html', 
                { "CURR": f"{hashcode}/{dirs[0]}", "PREV": f"{hashcode}/{dirs[1]}" }
            )
        else:
            return HttpResponse("make sure we have 2 folder crawled")
    except:
        print(traceback.format_exc())
        return HttpResponse(status=500)

