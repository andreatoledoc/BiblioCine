from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from AppBiblioCine import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('libros/', views.libros, name='Libros'),
    path('comentarioLibros/', views.comentarioLibros, name='ComentarioLibros'),
    #path('libroFormulario/', views.libroFormulario, name='LibroFormulario'),
    path('peliculas/', views.peliculas, name='Peliculas'),
    #path('peliculaFormulario/', views.peliculaFormulario, name='PeliculaFormulario'),
    path('busquedaAutor/', views.busquedaAutor, name='BusquedaAutor'),
    path('buscar/', views.buscar),
    path( 'leerLibros/', views.leerLibros, name='LeerLibros'),
]
