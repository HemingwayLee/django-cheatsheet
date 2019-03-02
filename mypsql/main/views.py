from django.http import HttpResponse
from django.db import connection
from .models import Clients

def show_all(request):
  output = ""
  for val in Clients.objects.all().values():
    output += str(val['id']) + " " + val['name'] + " " + str(val['age']) + "<br>"

  return HttpResponse(output)


def add_users(request):
    # in Django ORM, there is no truncate
    #  We need to use delete or sql script
    Clients.objects.all().delete()

    clients = [
        { "name":"James", "age":26, "dob":"1985-04-14" }, 
        { "name":"Kenny", "age":28, "dob":"1985-04-14" }, 
        { "name":"Rose", "age":31, "dob":"1987-04-01" },
        { "name":"Lee", "age":33, "dob":"1990-08-15" }, 
        { "name":"Bot", "age":1, "dob":"2019-02-20" }, 
    ]

    objs = [
        Clients(
            name=c["name"],
            age=c["age"],
            dob=c["dob"],
        ) for c in clients
    ]
    
    Clients.objects.bulk_create(objs)

    return HttpResponse("created", status=200)

def run_sql(request):    
    cursor = connection.cursor()
    cursor.execute('TRUNCATE TABLE "{0}"'.format(Clients._meta.db_table))

    return HttpResponse("truncated", status=200)

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

