from django.contrib import admin
from .models import Dispositivo, GrupoDispositivo, extraData

admin.site.register(Dispositivo)
admin.site.register(GrupoDispositivo)
admin.site.register(extraData)
