from django.db import models

class LoginFailedIpTable(models.Model):
    ip = models.TextField()
    retry = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
