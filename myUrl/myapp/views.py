from django.http import HttpResponse

def hello(request):
  return HttpResponse("hello, request")

def integer(request, myid):
  return HttpResponse("Hello, my id is " + str(myid))

def multiple(request, myid, name):
  return HttpResponse("Hello, %s. my id is %s" % (name, str(myid)))

# we need to put 002 on url, but it will show 2 in response
def three(request, num):
  return HttpResponse("Hello, my num is %s" % str(num))