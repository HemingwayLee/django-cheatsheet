from django.db import models
from django.conf import settings


class Entity(models.Model):
    dt = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

class Office(models.Model):
    address = models.CharField(max_length=2048)

    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

