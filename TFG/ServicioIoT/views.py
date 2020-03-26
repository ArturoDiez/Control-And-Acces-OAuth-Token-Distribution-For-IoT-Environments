# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
#from rest_framework import viewsets, renderers
from .models import Dispositivo, GrupoDispositivo
#from .serializers import DispositivoSerializer, GrupoDispositivoSerializer
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import GrupoDispositivoForm, DispositivoForm

# Create your views here.
@login_required
def index(request):
    GrupoDispositivo_list = GrupoDispositivo.objects.order_by('id')

    form = GrupoDispositivoForm()

    context = {'GrupoDispositivo_list' : GrupoDispositivo_list, 'form' : form}

    return render(request, 'index.html', context)

@require_POST
def addGrupoDispositivo(request):
    form = GrupoDispositivoForm(request.POST)

    new_grupodispositivo = GrupoDispositivo(nombre=request.POST['nombre'])
    new_grupodispositivo.save()

    return redirect('index')

@login_required
def indexDispositivo(request, GrupoDispositivo_id):
    Gp = GrupoDispositivo.objects.get(pk=GrupoDispositivo_id)

    Dispositivo_list = Dispositivo.objects.order_by('id')

    form = DispositivoForm()

    context = {'GrupoDispositivo': Gp,'Dispositivo_list' : Dispositivo_list, 'form' : form}

    return render(request, 'indexDispositivo.html', context)

@require_POST
def addDispositivo(request, GrupoDispositivo_id):
    form = DispositivoForm(request.POST)

    new_dispositivo = Dispositivo()

    username = request.user

    Gp = GrupoDispositivo.objects.get(pk=GrupoDispositivo_id)
    new_dispositivo.nombre = request.POST['nombre']
    new_dispositivo.descripcion = request.POST['descripcion']
    new_dispositivo.propietario = username
    new_dispositivo.grupo = Gp
    # new_dispositivo.authorizationCode = blank
    # new_dispositivo.accesToken = blank
    new_dispositivo.save()

    return redirect('indexDispositivo', GrupoDispositivo_id)

def deleteGrupo(request, GrupoDispositivo_id):
    GrupoDispositivo.objects.filter(pk=GrupoDispositivo_id).delete()

    return redirect('index')

@login_required
def pedirToken(request, Dispositivo_id, GrupoDispositivo_id):

    Dp = Dispositivo.objects.get(pk=Dispositivo_id)

    Gp = GrupoDispositivo.objects.get(pk=GrupoDispositivo_id)

    context = {'Dispositivo': Dp, 'GrupoDispositivo': Gp}

    return render(request, 'pedirToken.html', context)

def deleteDispositivo(request, Dispositivo_id, GrupoDispositivo_id):
    Dispositivo.objects.filter(pk=Dispositivo_id).delete()

    return redirect('indexDispositivo', GrupoDispositivo_id)

#class DispositivoView(LoginRequiredMixin,View):
#    queryset = Dispositivo.objects.all()
#    serializer_class = DispositivoSerializer

#class GrupoDispositivoView(LoginRequiredMixin,View):
#    queryset = GrupoDispositivo.objects.all()
#    serializer_class = GrupoDispositivoSerializer
