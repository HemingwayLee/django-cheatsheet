from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

@require_http_methods(["GET"])
def bulk(request):
    stds = [
        {"name":"James", "age":26}, 
        {"name":"Kenny", "age":28}, 
        {"name":"Lee", "age":33}, 
    ]

    objs = [
        Student(
            name=std["name"],
            age=std["age"]
        ) for std in stds
    ]
    
    Student.objects.bulk_create(objs)

    return HttpResponse("inserted !!")

@require_http_methods(["GET"])
def show(request):
    output = ""
    for val in Student.objects.all().values():
        output += str(val['id']) + " " + val['name'] + " " + str(val['age']) + "<br>"

    return HttpResponse(output)

