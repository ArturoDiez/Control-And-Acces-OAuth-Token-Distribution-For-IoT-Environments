from django import forms

from .models import GrupoDispositivo, Dispositivo, extraData

#aria-label: ayuda a saber que es, pero no aparece en la web

class extraDataForm(forms.Form):
        client_id = forms.CharField(max_length=100,
            widget=forms.TextInput(
               attrs={'class' : 'form-control', 'placeholder' : 'ID Cliente', 'aria-label' : 'extraData', 'aria-describedby' : 'add-btn'}))
        client_secret = forms.CharField(max_length=100,
            widget=forms.TextInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Secreto de Cliente', 'aria-label' : 'extraData', 'aria-describedby' : 'add-btn'}))

class GrupoDispositivoForm(forms.Form):
    nombre = forms.CharField(max_length=40,
        widget=forms.TextInput(
           attrs={'class' : 'form-control', 'placeholder' : 'Nombre del grupo', 'aria-label' : 'GrupoDispositivo', 'aria-describedby' : 'add-btn'}))

class DispositivoForm(forms.Form):
    nombre = forms.CharField(max_length=40,
        widget=forms.TextInput(
           attrs={'class' : 'form-control', 'placeholder' : 'Nombre del Dispositivo', 'aria-label' : 'Dispositivo', 'aria-describedby' : 'add-btn'}))
    descripcion = forms.CharField(
        widget=forms.TextInput(
           attrs={'class' : 'form-control', 'placeholder' : 'Descripcion del Dispositivo', 'aria-label' : 'Dispositivo', 'aria-describedby' : 'add-btn'}))
    grupo = forms.CharField(widget=forms.HiddenInput())
    propietario = forms.CharField(widget=forms.HiddenInput())
    token = forms.CharField(widget=forms.HiddenInput())
    link = forms.CharField(widget=forms.HiddenInput())
    datos = forms.CharField(widget=forms.HiddenInput())
