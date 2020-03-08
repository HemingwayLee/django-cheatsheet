from django.http import HttpResponse
from .models import Person


def insert(request):
  p = Person(fname="James", lname="Lee", age=26)
  p.save()
  p = Person(fname="Kenny", lname="Lee", age=28)
  p.save()
  p = Person(fname="Kristof", lname="Lee", age=25)
  p.save()

  return HttpResponse("Created!!")

def show(request):
  output = ""
  for p in Person.objects.raw("SELECT * FROM myapp_person WHERE id BETWEEN 2 AND 3;"):
    output += str(p.id) + " " + p.fname + " " + p.lname + "<br>"

  return HttpResponse(output)

