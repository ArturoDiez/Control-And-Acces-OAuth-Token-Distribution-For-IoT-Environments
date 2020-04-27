import os
from authlib.integrations.django_client import OAuth
from django.shortcuts import render, redirect
from .models import Dispositivo, GrupoDispositivo, extraData
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from .forms import GrupoDispositivoForm, DispositivoForm, extraDataForm
from django.http import HttpResponse, HttpRequest
import requests

oauth = OAuth()

os.environ.setdefault('AUTHLIB_INSECURE_TRANSPORT', '1')

REDIRECT_URI = 'http://127.0.0.1:8000/callback'

auth0 = oauth.register(
    'token acceso',
    client_id='0',
    client_secret='0',
    api_base_url='http://127.0.0.1:5000',
    access_token_url='http://127.0.0.1:5000/oauth/token',
    authorize_url='http://127.0.0.1:5000/oauth/authorize',
    client_kwargs={
        'scope': 'read',
    },
)

#@login_required
#def extraData(request):
#    usuario = request.user
#
#    form = extraDataForm()
#
#    context = {'form' : form, 'usuario': usuario}
#
#    return render(request, 'extraData.html', context)


#@require_POST
#@login_required
#def addExtraData(request):
#    form = extraDataForm(request.POST)
#
#    new_data = extraData()
#
#    new_data.client_id = request.POST['client_id']
#    new_data.client_secret = request.POST['client_secret']
#    new_data.save()
#    return redirect('extraData.html')

@login_required
def pedirToken(request):
    user_now = request.user

    usuario = extraData.objects.get(userid=user_now.id)

    auth0.client_id = usuario.client_id
    auth0.client_secret = usuario.client_secret
    #Pasando datos al server para recibir el codigo
    #parametros = {'client_id':,'redirect_uri': 'http://127.0.0.1:8000/api/','response_type':'token'}
    #r = requests.get('http://localhost:8081/oauth/authorize?', params = parametros)

    return auth0.authorize_redirect(request,redirect_uri=REDIRECT_URI)

@login_required
def callback(request):
    user_now = request.user

    usuario = extraData.objects.get(userid=user_now.id)

    token = auth0.authorize_acces_token()

    print(token)
    usuario.token = token
    usuario.save()

    GrupoDispositivo_list = GrupoDispositivo.objects.order_by('id')

    form = GrupoDispositivoForm()

    context = {'GrupoDispositivo_list' : GrupoDispositivo_list, 'form' : form, 'usuario': usuario}

    return render(request, 'index.html', context)
