from django.urls import path

from . import views

urlpatterns = [
    path('show/', views.show_all),
    path('delete/<int:qid>', views.delete),
    path('update/<int:qid>/<str:name>', views.update),
    path('update2/<str:name>/<int:age>', views.update2),
    path('insert/<str:name>/<int:age>', views.insert),
]