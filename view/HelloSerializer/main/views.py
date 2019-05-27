from django.http import JsonResponse
from .models import Team
from .serializers import TeamSerializer

def hello(request):
    team = Team(name="Team A", description="This is team A")
    ser = TeamSerializer(team)

    return JsonResponse(ser.data)

