from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .models import Person, Entry


def insert(request):
    user = get_user_model().objects.filter(id=1)
    e = Entry(name='AAA', author=user.first())
    e.save()

    entry = Entry.objects.filter(author=user.first())

    p = Person(fname="James", lname="Lee", age=26, entry=entry.first())
    p.save()
    p = Person(fname="Kenny", lname="Lee", age=28, entry=entry.first())
    p.save()
    p = Person(fname="Kristof", lname="Lee", age=25, entry=entry.first())
    p.save()
    p = Person(fname="Kristof", lname="New", age=22, entry=entry.first())
    p.save()
    p = Person(fname="Kenny", lname="New", age=26, entry=entry.first())
    p.save()

    return HttpResponse("Created!!")

def show(request):
    output = ""
    for p in Person.objects.raw("SELECT * FROM myapp_person WHERE id BETWEEN 2 AND 4;"):
        output += str(p.id) + " " + p.fname + " " + p.lname + "<br>"

    return HttpResponse(output)

def join(request):
    query = Person.objects.raw("""
        SELECT * FROM myapp_person AS mp 
        INNER JOIN myapp_entry AS me 
        ON mp.entry_id = me.id
        WHERE mp.id BETWEEN 1 AND 3;
    """)

    output = ""
    for p in query:
        output += str(p.id) + " " + p.fname + " " + p.lname + "<br>"

    return HttpResponse(output)

def latest(request):
    query = Person.objects.raw("""
        SELECT mp.* FROM myapp_person AS mp 
        INNER JOIN 
        (
            SELECT DISTINCT fname, MAX(id) AS mid FROM myapp_person
            GROUP BY fname
        ) AS tmp
        ON mp.id = tmp.mid
        INNER JOIN myapp_entry AS me 
        ON mp.entry_id = me.id
        WHERE me.author_id = 1;
    """)

    output = ""
    for p in query:
        output += str(p.id) + " " + p.fname + " " + p.lname + "<br>"

    return HttpResponse(output)


def count(request):
    query = Person.objects.raw("""
        SELECT mp.* FROM myapp_person AS mp 
        INNER JOIN 
        (
            SELECT DISTINCT fname, MAX(id) AS mid FROM myapp_person
            GROUP BY fname
        ) AS tmp
        ON mp.id = tmp.mid
        INNER JOIN myapp_entry AS me 
        ON mp.entry_id = me.id
        WHERE me.author_id = 1;
    """)

    output = ""
    p = query[0]
    output += str(p.id) + " " + p.fname + " " + p.lname + "<br>"

    return HttpResponse(f"{len(query)}, first: {output}")

def select_join(request):
    query = Person.objects.select_related("entry").raw("""
        SELECT * FROM myapp_person AS mp 
        INNER JOIN myapp_entry AS me 
        ON mp.entry_id = me.id
        WHERE mp.id BETWEEN 1 AND 3;
    """)

    print(len(query))

    output = ""
    for p in query:
        output += str(p.id) + " " + p.fname + " " + p.lname + " " + p.name + "<br>"

    return HttpResponse(output)


