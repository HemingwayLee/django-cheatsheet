from django.shortcuts import render
from django.contrib.auth.models import User

def hello(request):
    return render(request, 'helloworld.html')

def hello_context(request, myname):
    ct = { "name": myname }
    return render(request, 'hellocontext.html', ct)

def more_template(request):
    users = User.objects.filter(is_staff=True).values()
    ct = { "users": users }
    return render(request, 'hellomore.html', ct)

def base(request):
    return render(request, 'index.html')

def include(request):
    return render(request, 'container.html')