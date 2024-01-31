from django.contrib import admin
from .models import Cliente, Perro

class PerroInline(admin.TabularInline):
    model = Perro
    extra = 0

class ClienteAdmin(admin.ModelAdmin):
    inlines = [PerroInline]

admin.site.register(Cliente, ClienteAdmin)
