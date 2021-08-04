from django.db import models
from django.conf import settings

class Entry(models.Model):
    dt = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=128)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

class Person(models.Model):
    fname = models.CharField(max_length=128)
    lname = models.CharField(max_length=128)
    age = models.IntegerField()

    entry = models.ForeignKey(
        Entry,
        on_delete=models.CASCADE,
    )
