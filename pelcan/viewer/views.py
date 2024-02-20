from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import requires_csrf_token
from .models import Cita, Perro, Cliente
from .forms import ClienteForm
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

@requires_csrf_token
def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            telefono = form.cleaned_data["telefono"]
            email = form.cleaned_data["email"]

            new = Cliente(nombre=nombre, apellido=apellido, telefono=telefono, email=email)
            new.save()

            return cliente(request, new.id)
        else:
            return render(request, "viewer/cliente_new.html", {"form": form})
    else:
        return render(request, "viewer/cliente_new.html")

def calendario(request):
    citas = Cita.objects.all()
    context = {"citas": citas}

    return render(request, "viewer/calendario.html", context)

def citas(request):
    if request.method == "POST":
        fecha = request.POST.get("fecha")
        hora = request.POST.get("hora")
        horaFin = request.POST.get("horaFin")
        perro = request.POST.get("perro")
        duenho = request.POST.get("duenho")

        cita = Cita(fecha=fecha, hora=hora, horaFin=horaFin, perro_id=perro, duenho_id=duenho)
        cita.save()
        
        citas = Cita.objects.all()
        context = {"citas": citas, "success": True}
        return render(request, "viewer/citas.html", context)
    else:
        citas = Cita.objects.all()
        context = {"citas": citas}
        return render(request, "viewer/citas.html", context)