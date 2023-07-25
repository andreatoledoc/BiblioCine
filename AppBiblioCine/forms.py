from django import forms
from .models import Libro
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

class ComentarioLibroFormulario (forms.Form):
    libro = forms.ModelChoiceField(queryset=Libro.objects.all())
    nombre = forms.CharField()
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

#Registro

class UserRegisterForm (UserCreationForm):
    email = forms.EmailField()
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

#Editar perfil

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}


