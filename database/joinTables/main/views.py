import uuid
import random
import decimal
from time import sleep
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Entity, Office

@login_required(login_url='/admin/')
def hello(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM main_entity;")
        data = cursor.fetchall()

    output = ""
    for d in data:
        output += str(d[0]) + " " + d[1].strftime("%H:%M:%S") + " " + d[2] + "<br>"

    return HttpResponse(output)

@login_required(login_url='/admin/')
def hello2(request):
    query = Entity.objects.all()
    print(query.query)

    htmlCode = "<table border='1'><thead><tr><td>id</td><td>address</td><td>entity_name</td></tr></thead><tbody>"
    for val in query.values():
        print(val)
        htmlCode += "<tr>"
        htmlCode += f"<td>{val['id']}</td>"
        htmlCode += f"<td>{val['dt'].strftime('%H:%M:%S')}</td>"
        htmlCode += f"<td>{val['name']}</td>"
        htmlCode += "</tr>"
    htmlCode += "</tbody></table>"

    return HttpResponse(htmlCode)


@login_required(login_url='/admin/')
def join(request):
    query = Office.objects.select_related("entity")
    print(query.query)

    # Must put `entity__name` in values
    htmlCode = "<table border='1'><thead><tr><td>id</td><td>address</td><td>entity_name</td></tr></thead><tbody>"
    for val in query.values("id", "address", "entity__name"):
        print(val)
        htmlCode += "<tr>"
        htmlCode += f"<td>{val['id']}</td>"
        htmlCode += f"<td>{val['address']}</td>"
        htmlCode += f"<td>{val['entity__name']}</td>"
        htmlCode += "</tr>"
    htmlCode += "</tbody></table>"

    return HttpResponse(htmlCode)


@login_required(login_url='/admin/')
def joinfilter(request):
    query = Office.objects.select_related("entity").filter(entity__name="a")
    print(query.query)

    htmlCode = "<table border='1'><thead><tr><td>id</td><td>address</td><td>entity_name</td></tr></thead><tbody>"
    for val in query.values("id", "address", "entity__name"):
        print(val)
        htmlCode += "<tr>"
        htmlCode += f"<td>{val['id']}</td>"
        htmlCode += f"<td>{val['address']}</td>"
        htmlCode += f"<td>{val['entity__name']}</td>"
        htmlCode += "</tr>"
    htmlCode += "</tbody></table>"

    return HttpResponse(htmlCode)


@login_required(login_url='/admin/')
def joinfilteruser(request):
    query = Office.objects.select_related("entity").filter(address='address_1', entity__author=request.user)
    print(query.query)

    htmlCode = "<table border='1'><thead><tr><td>id</td><td>address</td><td>entity_name</td></tr></thead><tbody>"
    for val in query.values("id", "address", "entity__name"):
        print(val)
        htmlCode += "<tr>"
        htmlCode += f"<td>{val['id']}</td>"
        htmlCode += f"<td>{val['address']}</td>"
        htmlCode += f"<td>{val['entity__name']}</td>"
        htmlCode += "</tr>"
    htmlCode += "</tbody></table>"

    return HttpResponse(htmlCode)


@login_required(login_url='/admin/')
def joinfilteruserid(request):
    # Root user
    user = get_user_model().objects.filter(id=1)
    query = Office.objects.select_related("entity").filter(address='address_1', entity__author=user.first())
    print(query.query)

    htmlCode = "<table border='1'><thead><tr><td>id</td><td>address</td><td>entity_name</td></tr></thead><tbody>"
    for val in query.values("id", "address", "entity__name"):
        print(val)
        htmlCode += "<tr>"
        htmlCode += f"<td>{val['id']}</td>"
        htmlCode += f"<td>{val['address']}</td>"
        htmlCode += f"<td>{val['entity__name']}</td>"
        htmlCode += "</tr>"
    htmlCode += "</tbody></table>"

    return HttpResponse(htmlCode)

@login_required(login_url='/admin/')
def insert(request):
    for i in range(random.randint(10, 50)):
        sleep(decimal.Decimal(random.randrange(50, 300))/1000)

        et = Entity(
            name=uuid.uuid4().hex[:1],
            author=request.user)
        et.save()

        of1 = Office(
            address="address_1",
            entity=et,
        )
        of1.save()

        of2 = Office(
            address="address_2",
            entity=et,
        )
        of2.save()

    return HttpResponse("Created!!")
