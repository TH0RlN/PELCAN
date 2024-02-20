from typing import Any
from django import forms
from django.forms import Form

class CitaForm(Form):
    fecha = forms.DateField()
    hora = forms.TimeField()
    horaFin = forms.TimeField()
    perro = forms.IntegerField()
    duenho = forms.IntegerField()

class ClienteForm(Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=15)
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        telefono = cleaned_data.get("telefono")
        if len(telefono) < 8:
            raise forms.ValidationError("El telefono debe tener al menos 8 digitos")
        return cleaned_data
