from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=256)
    description = serializers.CharField(max_length=256)
