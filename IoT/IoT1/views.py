from django.shortcuts import render, redirect
from .models import Dispositivo
from django.views.decorators.csrf import ensure_csrf_cookie

import requests
import json
import Cryptodome
import base64
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP, AES
from Cryptodome.Random import get_random_bytes
from base64 import b64encode
import requests
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    disp = Dispositivo.objects.get(pk=1)

    context = {'Dispositivo':disp}

    return render(request, 'index.html',context)


def getToken(request):
    token = request.POST.get('token')
    disp = Dispositivo.objects.get(pk=1)

    privk = RSA.import_key(open('private.pem').read())
    cipher_rsa= PKCS1_OAEP.new(privk)

    t = token.encode('latin-1')

    length=len(t)

    print(t)
    print(length)

    #t = pad(token)
    c = cipher_rsa.decrypt(t)
    tok = c.decode('utf-8')

    disp.token = tok
    disp.save()

    return redirect('index')


def sendData(request):
    disp = Dispositivo.objects.get(pk=1)
    #El token debe ser de 48 bytes para poder usarlo en AES
    t = pad(disp.token)
    us_token = t.encode('utf-8')
    data = disp.datos.encode('utf-8')

    recipient_key = RSA.import_key(open('receiver25.pem').read())

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_token_key = cipher_rsa.encrypt(us_token)

    nonce = get_random_bytes(16)
    cipher_aes = AES.new(us_token, AES.MODE_SIV, nonce = nonce)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    json_k = ['nonce','enc_token_key','ciphertext','tag']
    json_v = [b64encode(x).decode('utf-8') for x in (nonce, enc_token_key, ciphertext, tag)]
    result = json.dumps(dict(zip(json_k,json_v)))
    print(result)

    datos = {'data': result, 'Dispositivo_id': '25', 'GrupoDispositivo_id': '23'}

    r = requests.post('http://127.0.0.1:8000/app/23/25/recibirDatos', data = datos)

    return redirect('index')

def pad(s):
    return s + ((48-len(s) % 48) * '{')

def estadoToken(request):
    disp = Dispositivo.objects.get(pk=1)
    estado = request.POST.get('token')
    print(estado)
    disp.estado_token = estado
    disp.save()

    context = {'Dispositivo':disp}

    return render(request, 'index.html',context)
