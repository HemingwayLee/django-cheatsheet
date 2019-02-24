from django.http import HttpResponse

def sp(request):
    return HttpResponse("sp", status=200)

def join(request):
    return HttpResponse("join", status=200)

def atomic(request):
    return HttpResponse("atomic", status=200)

def like(request):
    return HttpResponse("join", status=200)

def raw(request):
    return HttpResponse("raw", status=200)

def raw_param(request):
    return HttpResponse("raw2", status=200)

def sort(request):
    return HttpResponse("sort", status=200)

def order(request):
    return HttpResponse("order", status=200)

def count(request):
    return HttpResponse("count", status=200)

def group(request):
    return HttpResponse("group", status=200)

