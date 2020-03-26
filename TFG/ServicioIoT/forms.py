from django import forms

from .models import GrupoDispositivo, Dispositivo

#aria-label: ayuda a saber que es, pero no aparece en la web

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
    # authorizationCode= forms.CharField(widget=forms.HiddenInput())
    # accesToken = forms.CharField(widget=forms.HiddenInput())
