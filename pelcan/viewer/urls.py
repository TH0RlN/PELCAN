from django.urls import path

from . import views

app_name = "viewer"
urlpatterns = [
    path("", views.index),
    path("perro/", views.perros),
    path("perro/<int:perro_id>/", views.perro),
    path("perro/new/<int:duenho_id>/", views.perro_new),
    path("cliente/", views.clientes),
    path("cliente/<int:cliente_id>/", views.cliente),
    path("cliente/new/", views.cliente_new),
    path("calendario/", views.calendario),
    path("citas/", views.citas),
]