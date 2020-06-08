from django.http import HttpResponse, JsonResponse
from django.db import connection

def showAll(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM auth_user;''')
    # rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    allRows = [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]

    return JsonResponse(allRows, safe=False, status=200)
