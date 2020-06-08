from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import MyUser
from django.db import connection

def doSignup(request):
    MyUser.objects.create_user("abc@gmail.com", "1985-04-14", "test")

    return HttpResponse("created!", status=200)

def showAll(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM main_myuser;''')
    # rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    allRows = [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]

    return JsonResponse(allRows, safe=False, status=200)
