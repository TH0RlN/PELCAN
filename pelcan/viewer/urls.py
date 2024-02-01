from django.urls import path

from . import views

app_name = "viewer"
urlpatterns = [
    path("", views.index),
    path("perro/", views.perros),
    path("perro/<int:perro_id>/", views.perro),
]