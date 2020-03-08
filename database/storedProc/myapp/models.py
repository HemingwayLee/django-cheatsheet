from django.db import models

class Person(models.Model):
  fname = models.CharField(max_length=128)
  lname = models.CharField(max_length=128)
  age = models.IntegerField()
