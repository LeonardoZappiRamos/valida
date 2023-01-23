from django.urls import path, include

from . import views 

urlpatterns = [
    path('api/', views.lista_ativos, name='index'),
]
