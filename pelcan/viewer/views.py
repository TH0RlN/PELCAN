from django.shortcuts import render, get_object_or_404
from .models import Cita, Perro, Cliente
from calendar import HTMLCalendar
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
    fotoUrl = '/'.join(perro.foto.name.split('/')[2:])
    context = {"perro": perro, "fotoUrl": fotoUrl}

    return render(request, "viewer/perro_details.html", context)

def clientes(request):
    clientes = Cliente.objects.all()
    context = {"clientes": clientes}

    return render(request, "viewer/clientes.html", context)

def cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    perros = Perro.objects.filter(duenho=cliente)
    context = {"cliente": cliente, "perros": perros}

    return render(request, "viewer/cliente_details.html", context)

def calendario(request):
    citas = Cita.objects.all()
    context = {"citas": citas}

    return render(request, "viewer/calendario.html", context)