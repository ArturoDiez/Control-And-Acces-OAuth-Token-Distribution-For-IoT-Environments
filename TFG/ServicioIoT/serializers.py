from rest_framework import serializers
from .models import Dispositivo, GrupoDispositivo

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = ('nombre','descripcion','grupo','url','propietario','id')

class GrupoDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoDispositivo
        fields = ('nombre','url','id')
