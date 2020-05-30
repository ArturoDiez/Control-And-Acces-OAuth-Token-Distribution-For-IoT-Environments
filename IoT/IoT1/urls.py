from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getToken', views.getToken, name='getToken'),
    path('sendData', views.sendData, name='sendData'),
    path('estadoToken', views.estadoToken, name='estadoToken')
]
