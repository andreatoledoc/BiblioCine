from django.shortcuts import render
from AppBiblioCine.models import Libro, Pelicula
from django.http import HttpResponse

#Inicio

def inicio(request):
    return render (request, "AppBiblioCine/inicio.html")

#Peliculas

def libros(request):
    return render (request, "AppBiblioCine/libros.html")

#Libros

def peliculas(request):
    return render (request, "AppBiblioCine/peliculas.html")
