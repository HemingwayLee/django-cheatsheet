import os
from django.http import HttpResponse
from dotenv import load_dotenv

def index(request):
    load_dotenv("./changePort/.env")
    print(os.environ.get("WEBAPP_PORT"))

    return HttpResponse(200)