import os
from authlib.integrations.django_client import OAuth
from django.shortcuts import render, redirect
from .models import Dispositivo, GrupoDispositivo, extraData
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from oauthlib.oauth2 import WebApplicationClient
from django.views.decorators.http import require_POST
from .forms import GrupoDispositivoForm, DispositivoForm, extraDataForm
from django.http import HttpResponse, HttpRequest
from requests_oauthlib import OAuth2Session
from django.views.decorators.csrf import csrf_exempt
import requests
import json
import Cryptodome
import base64
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from base64 import b64decode

oauth = OAuth()

os.environ.setdefault('AUTHLIB_INSECURE_TRANSPORT', '1')

@login_required
def pedirCode(request):
    user_now = request.user

    usuario = extraData.objects.get(userid=user_now.id)

    #Pasando datos al server para recibir el codigo
    parametros = {'response_type':'code','client_id':usuario.client_id,'redirect_uri': 'http://127.0.0.1:8000/app/callback','scope':'read'}
    r = requests.post('http://localhost:8080/web/authorize?', params = parametros)

    return redirect(r.url)

@login_required
def callback(request):
    user_now = request.user

    usuario = extraData.objects.get(userid=user_now.id)

    c_s = usuario.client_secret
    c_id = usuario.client_id

    code = request.GET.get('code','')


    if code != '':

        #print(code)
        usuario.code = code
        usuario.save()

        s = OAuth2Session(client_id=c_id,redirect_uri='http://127.0.0.1:8000/app/callback', scope='read')
        token = s.fetch_token(token_url='http://localhost:8080/v1/oauth/tokens?', client_secret=c_s,authorization_response=request.build_absolute_uri())

    #print(token)

    usuario.token = token['access_token']
    usuario.save()
    a= usuario.token

    return redirect('index')
