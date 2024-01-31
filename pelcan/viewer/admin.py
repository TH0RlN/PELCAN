from django.contrib import admin
from .models import Cliente, Perro, Cita

class PerroInline(admin.TabularInline):
    model = Perro
    extra = 0

class ClienteAdmin(admin.ModelAdmin):
    inlines = [PerroInline]

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Cita)
