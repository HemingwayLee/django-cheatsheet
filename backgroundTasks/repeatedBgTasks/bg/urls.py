from django.urls import path
from . import views

urlpatterns = [
    path('', views.callme),
    path('repeat/', views.callRepeat),
    path('ontime/', views.callOnTime),
]