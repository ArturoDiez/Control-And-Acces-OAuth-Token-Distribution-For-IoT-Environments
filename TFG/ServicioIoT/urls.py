from django.urls import path, include
from . import views, oauth2

urlpatterns = [
    path('', views.index, name='index'),
    #path('extraData',oauth2.extraData, name='extraData'),
    #path('extraData/addExtraData/', oauth2.addExtraData, name='addExtraData'),
    path('callback', oauth2.callback, name='callback'),
    path('pedirCode', oauth2.pedirCode, name='pedirCode'),
    path('addGrupoDispositivo/', views.addGrupoDispositivo, name='addGrupoDispositivo'),
    path('<GrupoDispositivo_id>', views.indexGrupoDispositivo, name='indexGrupoDispositivo'),
    path('<GrupoDispositivo_id>/addDispositivo/', views.addDispositivo, name='addDispositivo'),
    path('<GrupoDispositivo_id>/deleteGrupo/', views.deleteGrupo, name='deleteGrupo'),
    path('<GrupoDispositivo_id>/<Dispositivo_id>/', views.indexDispositivo, name='indexDispositivo'),
    path('<GrupoDispositivo_id>/<Dispositivo_id>/deleteDispositivo/', views.deleteDispositivo, name='deleteDispositivo'),
    path('<GrupoDispositivo_id>/<Dispositivo_id>/tokenDispositivo/', views.tokenDispositivo, name='tokenDispositivo'),
    path('<GrupoDispositivo_id>/<Dispositivo_id>/recibirDatos', views.recibirDatos, name='recibirDatos'),
]
