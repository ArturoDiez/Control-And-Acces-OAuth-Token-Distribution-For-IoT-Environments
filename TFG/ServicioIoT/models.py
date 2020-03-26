
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GrupoDispositivo (models.Model):
    nombre = models.CharField(max_length=100, unique = True)

    def __str__(self):
        return self.nombre

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=50, blank = False)
    descripcion = models.CharField(max_length=200, default='Descripcion')
    propietario = models.ForeignKey(User,to_field='username', on_delete=models.CASCADE, default='Api')
    grupo = models.ForeignKey(GrupoDispositivo, on_delete=models.SET_DEFAULT, null = True, related_name='nombregrupo', default='1')
    # authorizationCode = models.CharField(max_length = 1000, default = 'AuthorizationCode')
    # accesToken = models.CharField(max_length = 1000, default = 'AccesToken')

    def __str__(self):
        return self.nombre
