from django import forms
from .models import Libro, Pelicula
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

#Libros

class LibroFormulario(forms.Form):
    titulo = forms.CharField()
    autor = forms.CharField()
    año_publicacion = forms.IntegerField()
    editorial = forms.CharField()
    sinopsis = forms.CharField()
    genero = forms.CharField()
    idioma = forms.CharField()
    portada = forms.ImageField()
    recomendacion = forms.CharField()

class ComentarioLibroFormulario (forms.Form):
    libro = forms.ModelChoiceField(queryset=Libro.objects.all())
    #nombre = forms.ModelChoiceField(queryset=User.objects.all())
    comentario = forms.CharField()
    

#Peliculas

class PeliculaFormulario (forms.Form):
    titulo = forms.CharField()
    director = forms.CharField()
    año_lanzamiento = forms.IntegerField()
    sinopsis = forms.CharField()
    genero = forms.CharField()
    duracion = forms.IntegerField()
    portada = forms.ImageField()
    recomendacion = forms.CharField()

class ComentarioPeliculaFormulario (forms.Form):
    pelicula = forms.ModelChoiceField(queryset=Pelicula.objects.all())
    #nombre = forms.ModelChoiceField(queryset=User.objects.all())
    comentario = forms.CharField()



