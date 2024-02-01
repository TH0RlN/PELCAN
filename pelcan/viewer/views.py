from django.shortcuts import render, get_object_or_404
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

def perro(request, perro_id):
    perro = get_object_or_404(Perro, pk=perro_id)
    context = {"perro": perro}

    return render(request, "viewer/perro_details.html", context)