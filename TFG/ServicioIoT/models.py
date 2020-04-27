
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class extraData (models.Model):
    userid = models.OneToOneField(User, on_delete=models.CASCADE)
    client_id = models.CharField(max_length=100, unique = True)
    client_secret = models.CharField(max_length=100, unique = True)
    code = models.CharField(max_length=100, unique = True)
    token = models.CharField(max_length=100, unique = True)

    @receiver(post_save, sender=User)
    def create_user_extradata(sender, instance, created, **kwargs):
        if created:
            extraData.objects.create(user=instance)

        @receiver(post_save, sender=User)
        def save_user_extradata(sender, instance, **kwargs):
            instance.extraData.save()

    def __str__(self):
        return self.client_id

class GrupoDispositivo (models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=50, blank = False)
    descripcion = models.CharField(max_length=200, default='Descripcion')
    propietario = models.ForeignKey(User,to_field='username', on_delete=models.CASCADE, default='Api')
    grupo = models.ForeignKey(GrupoDispositivo, on_delete=models.SET_DEFAULT, null = True, related_name='nombregrupo', default='1')

    def __str__(self):
        return self.nombre
