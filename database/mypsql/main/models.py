from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)