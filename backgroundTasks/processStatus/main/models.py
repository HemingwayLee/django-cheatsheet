from django.db import models

class MyTask(models.Model):
    filename = models.TextField()
    status = models.IntegerField()
