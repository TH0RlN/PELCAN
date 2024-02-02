from django import forms
from django.forms import Form

class CitaForm(Form):
    fecha = forms.DateField()
    hora = forms.TimeField()
    horaFin = forms.TimeField()
    perro = forms.IntegerField()
    duenho = forms.IntegerField()
