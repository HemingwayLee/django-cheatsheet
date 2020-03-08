from django.http import HttpResponse
from django.db import connection
from .models import Person

def insert(request):
  p = Person(fname="James", lname="Lee", age=26)
  p.save()
  p = Person(fname="Kenny", lname="Lee", age=28)
  p.save()
  p = Person(fname="Kristof", lname="Lee", age=25)
  p.save()

  return HttpResponse("Created!!")

def show1(request):
  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM person_info;")
    data = cursor.fetchall()

  output = ""
  for p in data:
    output += str(p[0]) + " " + p[1] + " " + p[2] + "<br>"

  return HttpResponse(output)


def show2(request):
  with connection.cursor() as cursor:
    # `person_info` is view, callproc does not work
    # cursor.callproc("person_info")
    cursor.callproc("my_func") 
    data = cursor.fetchall()

  output = ""
  for p in data:
    output += str(p[0]) + " " + p[1] + " " + p[2] + "<br>"

  return HttpResponse(output)