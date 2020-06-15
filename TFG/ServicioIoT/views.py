# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Dispositivo, GrupoDispositivo, extraData
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import GrupoDispositivoForm, DispositivoForm, extraDataForm
from django.http import HttpResponse, HttpRequest
import requests
import json
import Cryptodome
import base64
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP, AES
from base64 import b64decode
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import time



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

    RSAkey = RSA.generate(2048)

    public_key = RSAkey.publickey().export_key()
    file_out = open("receiver{id}.pem".format(id=new_dispositivo.id),"wb")
    file_out.write(public_key)
    file_out.close()
    file_out = open("private{id}.pem".format(id=new_dispositivo.id),"wb")
    file_out.write(RSAkey.export_key())
    file_out.close()

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

@login_required
def tokenDispositivo(request, Dispositivo_id, GrupoDispositivo_id):
    Dp = Dispositivo.objects.get(pk=Dispositivo_id)
    Gp = GrupoDispositivo.objects.get(pk=GrupoDispositivo_id)

    user_now = request.user
    usuario = extraData.objects.get(userid=user_now.id)

    us_token = usuario.token.encode('utf-8')

    public_key = RSA.import_key(open("receiver{id}.pem".format(id=Dispositivo_id)).read())
    cipher_rsa = PKCS1_OAEP.new(public_key)
    a = cipher_rsa.encrypt(us_token)

    Dp.token = a
    Dp.save()
    #Lo enviamos en texto y no en bytes ya que causa problemas. Con latin-1 ya que utf-8 no reconoce algunos valores.
    b = a.decode('latin-1')

    r = requests.post(Dp.link+'getToken', data = {'token': b})

    return redirect('indexDispositivo', GrupoDispositivo_id, Dispositivo_id)

@csrf_exempt
def recibirDatos(request, Dispositivo_id, GrupoDispositivo_id):
    #Vemos quien es el usuario, ya que se necesitan algunos datos de cliente
    Dp = Dispositivo.objects.get(pk=Dispositivo_id)
    username = Dp.propietario
    id = User.objects.get(username=username)
    usuario = extraData.objects.get(userid=id)

    datos = request.POST.get('data')
    a = json.loads(datos)

    json_k = ['nonce','enc_token_key','ciphertext','tag']
    jv = {k:b64decode(a[k]) for k in json_k}

    #Desencriptando el token
    privk = RSA.import_key(open('private{id}.pem'.format(id=Dispositivo_id)).read())
    cipher_rsa= PKCS1_OAEP.new(privk)
    t = cipher_rsa.decrypt(jv['enc_token_key'])
    t2 = t.decode('utf-8')
    token = unpad(t2)

    #Se envia el token al servidor para ver si está activo
    auth= (usuario.client_id,usuario.client_secret)
    params= {'token': token, 'token_type_hint':'access_token'}
    r = requests.post('http://localhost:8080/v1/oauth/introspect',params= params, auth=auth)
    #print(r.status_code)
    f = r.json()
    #print(f)

    #Se hace por statu_code ya que solo da un 200 cuando el token está activo
    if r.status_code == 200:
        #Sacar el mensaje y guardarlo
        t = pad(token)
        us_token = t.encode('utf-8')
        cipher = AES.new(us_token, AES.MODE_SIV, nonce = jv['nonce'])
        plaintext= cipher.decrypt_and_verify(jv['ciphertext'],jv['tag'])
        texto = plaintext.decode('utf-8')
        Dp.datos= texto
        Dp.save()
        #print(texto)

        #Mandarle al dispositivo que todo bien
        requests.post(Dp.link+'estadoToken',data={'token':'Token activo'})

        return redirect('indexDispositivo', GrupoDispositivo_id, Dispositivo_id)

    else:
        #Mandar que mensaje mal o expirado a dispositivo
        requests.post(Dp.link+'estadoToken',data={'token':'Token inválido o expirado'})

        return redirect('indexDispositivo', GrupoDispositivo_id, Dispositivo_id)

    return redirect('indexDispositivo', GrupoDispositivo_id, Dispositivo_id)

#Añade bytes a la variable hasta que sea 48 o divisible por el
def pad(s):
    return s + ((48-len(s) % 48) * '{')

#Deshace lo hecho por pad
def unpad(s):
    l = s.count('{')
    return s[:len(s)-l]
