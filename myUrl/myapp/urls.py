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
    # return image
    path('image/', views.return_img),
    path('image/base64/', views.return_base64_img),
    path('show/', views.show_base64)
]