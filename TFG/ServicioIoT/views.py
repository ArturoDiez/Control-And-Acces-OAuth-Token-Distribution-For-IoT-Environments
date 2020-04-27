# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
#from rest_framework import viewsets, renderers
from .models import Dispositivo, GrupoDispositivo, extraData
#from .serializers import DispositivoSerializer, GrupoDispositivoSerializer
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import GrupoDispositivoForm, DispositivoForm, extraDataForm
from django.http import HttpResponse, HttpRequest
import requests
import json


# Create your views here.
@login_required
def index(request):
    usuario = request.user
    GrupoDispositivo_list = GrupoDispositivo.objects.order_by('id')

    form = GrupoDispositivoForm()

    context = {'GrupoDispositivo_list' : GrupoDispositivo_list, 'form' : form, 'usuario': usuario}

    return render(request, 'index.html', context)

@require_POST
def addGrupoDispositivo(request):
    form = GrupoDispositivoForm(request.POST)

    new_grupodispositivo = GrupoDispositivo(nombre=request.POST['nombre'])
    new_grupodispositivo.save()

    return redirect('index')

@login_required
def indexGrupoDispositivo(request, GrupoDispositivo_id):
    Gp = GrupoDispositivo.objects.get(pk=GrupoDispositivo_id)

    Dispositivo_list = Dispositivo.objects.order_by('id')

    form = DispositivoForm()

    context = {'GrupoDispositivo': Gp,'Dispositivo_list' : Dispositivo_list, 'form' : form}

    return render(request, 'indexGrupoDispositivo.html', context)

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
    new_dispositivo.save()

    return redirect('indexGrupoDispositivo', GrupoDispositivo_id)

@login_required
def deleteGrupo(request, GrupoDispositivo_id):
    GrupoDispositivo.objects.filter(pk=GrupoDispositivo_id).delete()

    return redirect('index')



@login_required
def deleteDispositivo(request, Dispositivo_id, GrupoDispositivo_id):
    Dispositivo.objects.filter(pk=Dispositivo_id).delete()

    return redirect('indexGrupoDispositivo', GrupoDispositivo_id)


@login_required
def indexDispositivo(request, Dispositivo_id, GrupoDispositivo_id):

    Dp = Dispositivo.objects.get(pk=Dispositivo_id)

    Gp = GrupoDispositivo.objects.get(pk=GrupoDispositivo_id)

    context = {'Dispositivo': Dp, 'GrupoDispositivo': Gp}

    return render(request, 'indexDispositivo.html', context)

#class DispositivoView(LoginRequiredMixin,View):
#    queryset = Dispositivo.objects.all()
#    serializer_class = DispositivoSerializer

#class GrupoDispositivoView(LoginRequiredMixin,View):
#    queryset = GrupoDispositivo.objects.all()
#    serializer_class = GrupoDispositivoSerializer
