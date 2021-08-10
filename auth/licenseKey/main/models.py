from django.db import models
from django.conf import settings

# NOTE: current design, one license key for all tenant users
class MyKey(models.Model):
    dt = models.DateTimeField(auto_now_add=True)
    tenant = models.CharField(max_length=128)
    page_count_limit = models.IntegerField()
    expired_date = models.DateTimeField()
    secret = models.CharField(max_length=16, unique=True)
    license_key = models.CharField(max_length=256)

class MyUser(models.Model):
    dt = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=128)
    mac = models.CharField(max_length=128, blank=True)

    key = models.ForeignKey(MyKey, on_delete=models.CASCADE)

