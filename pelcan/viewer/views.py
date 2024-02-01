from django.shortcuts import render
from .models import Cita, Perro, Cliente
import datetime

def index(request):
    citas_hoy = Cita.objects.filter(fecha=datetime.date.today())
    context = {"citas_hoy": citas_hoy}

    return render(request, "viewer/index.html", context)

def perros(request):
    perros = Perro.objects.all()
    context = {"perros": perros}

    return render(request, "viewer/perros.html", context)