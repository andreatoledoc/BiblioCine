from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from AppBiblioCine import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('libros/', views.libros, name='Libros'),
    path('peliculas/', views.peliculas, name='Peliculas'),
]
