import csv
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings


def index(request):
    return render(request, 'index.html')

def responseCsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="iris.csv"'

    writer = csv.writer(response)
    path = f"{settings.MEDIA_ROOT}/iris.csv"
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            writer.writerow(row)
    
    return response
