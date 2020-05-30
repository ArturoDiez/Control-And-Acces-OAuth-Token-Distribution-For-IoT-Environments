from django.db import models

# Create your models here.

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=50, blank = False)
    token = models.CharField(max_length=100,default='Esto no es un token')
    datos = models.CharField(max_length=10000, default='Datos del dispositivo')
    estado_token = models.CharField(max_length=50,default='---')

    def __str__(self):
        return self.nombre
