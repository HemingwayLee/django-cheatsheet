from django.db import models
from django.conf import settings

class MyKey(models.Model):
    dt = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    tenant = models.CharField(max_length=128)
    mac = models.CharField(max_length=128, blank=True)
    page_count_limit = models.IntegerField()
    expired_date = models.DateTimeField()
    secret = models.CharField(max_length=16, unique=True)
    license_key = models.CharField(max_length=256)
