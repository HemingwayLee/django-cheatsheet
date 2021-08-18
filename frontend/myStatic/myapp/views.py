from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.contrib.staticfiles.utils import get_files
from django.contrib.staticfiles.storage import StaticFilesStorage

# this can be access by `http://127.0.0.1:8000/move2root.js`
def root_js(request):
    print(settings.STATIC_ROOT)

    filename = settings.STATIC_ROOT + '/js/move2root.js'
    jsfile = open(filename, 'rb')
    response = HttpResponse(content=jsfile)
    response['Content-Type'] = 'text/javascript'
    response['Content-Disposition'] = 'attachment; filename="%s"' % (filename)
    return response


def show(request):
    return render(request, 'hello.html')

def use_css_js(request):
    return render(request, 'cssjs.html')

def get_media(request):
    print(settings.MEDIA_ROOT)

    with open(settings.MEDIA_ROOT + "/data.txt") as file:
        content = file.read()
        print(content)
        return HttpResponse(content, status=200)

def list_static(request):
    s = StaticFilesStorage()
    
    return JsonResponse(list(get_files(s, location='css')), safe=False)
