from django.db import models

class MyTask(models.Model):
    filename = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
