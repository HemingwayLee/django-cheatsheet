import time
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def handler404(request, exception):
    print(f"{request.path} 404, redirect...") 
    return render(request, 'hello.html', {
        'PAGE_URL': request.path
    })

def show(request):
    return render(request, 'hello.html', {
        'PAGE_URL': "/"
    })

def test(request):
    print(request.headers)

    return JsonResponse({"msg": "ok", "ts": str(time.time())})

# this can be access by `http://127.0.0.1:8000/hook.js`
def root_js(request):
    print(settings.STATIC_ROOT)

    filename = settings.STATIC_ROOT + '/js/hook.js'
    jsfile = open(filename, 'rb')
    response = HttpResponse(content=jsfile)
    response['Content-Type'] = 'text/javascript'
    response['Content-Disposition'] = 'attachment; filename="%s"' % (filename)
    return response

