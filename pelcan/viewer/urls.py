from django.urls import path

from . import views

app_name = "viewer"
urlpatterns = [
    path("", views.index),
    path("perro/", views.perros),
    path("perro/<int:perro_id>/", views.perro),
    path("cliente/", views.clientes),
    path("cliente/<int:cliente_id>/", views.cliente),
    path("calendario/", views.calendario),
]