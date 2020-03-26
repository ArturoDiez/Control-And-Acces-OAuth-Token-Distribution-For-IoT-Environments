from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addGrupoDispositivo/', views.addGrupoDispositivo, name='addGrupoDispositivo'),
    path('<GrupoDispositivo_id>', views.indexDispositivo, name='indexDispositivo'),
    path('<GrupoDispositivo_id>/addDispositivo/', views.addDispositivo, name='addDispositivo'),
    path('<GrupoDispositivo_id>/deleteGrupo/', views.deleteGrupo, name='deleteGrupo'),
    path('<GrupoDispositivo_id>/<Dispositivo_id>/', views.pedirToken, name='pedirToken'),
    path('<GrupoDispositivo_id>/<Dispositivo_id>/deleteDispositivo/', views.deleteDispositivo, name='deleteDispositivo'),
]
