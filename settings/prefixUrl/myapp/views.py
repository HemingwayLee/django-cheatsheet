from django.http import HttpResponse

def hello(request):
  return HttpResponse("Hello!!")

def hi(request):
  return HttpResponse("Hi")
