from django.shortcuts import render

def hello(request):
    return render(request, 'helloworld.html')

def hello_context(request):
    ct = { "age": 33 }
    return render(request, 'hellocontext.html', ct)