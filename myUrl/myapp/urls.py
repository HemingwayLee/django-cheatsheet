from django.urls import path, register_converter
from . import views, converters

register_converter(converters.ThreeDigitConverter, 'ddd')

urlpatterns = [
  path('', views.hello),
  # path converter
  path('integer/<int:myid>/', views.integer),
  path('mul/<int:myid>/<str:name>', views.multiple),
  # custom path converter
  path('custom/<ddd:num>/', views.three),
]