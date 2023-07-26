from django.shortcuts import render, redirect
from AppBiblioCine.models import Libro, Pelicula, ComentarioLibro, Avatar
from django.http import HttpResponse
from AppBiblioCine.forms import AvatarFormulario, UserEditForm, UserRegisterForm, LibroFormulario, PeliculaFormulario, ComentarioLibroFormulario
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy #Me permite que los objetos se carguen background
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

#Inicio
@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    print (avatares)
    return render(request, 'AppBiblioCine/inicio.html', {'url':avatares[0].imagen.url})

#Login
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contras = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contras)

            if user is not None:
                login(request, user)
                return render (request, 'AppBiblioCine/inicio.html', {'mensaje': f"Bienvenido {usuario}", 'user': user, 'login_success': True})

            else:
                return render(request, 'AppBiblioCine/inicio.html', {"mensaje": "Error, datos erroneos", 'login_success': False})
        else:
            return render(request, 'AppBiblioCine/inicio.html', {'mensaje': 'Error, formulario erroneo', 'form': form, 'login_success': False})
    
    form = AuthenticationForm()

    return render (request, 'AppBiblioCine/login.html', {'form': form})

#Registro
def register (request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            messages.success(request, f"Usuario {username} creado exitosamente.")
            return redirect('Inicio')  # Redireccionamos a la página de inicio
        
    else:
        form = UserRegisterForm()

    return render (request, "AppBiblioCine/registro.html", {"form":form})

#EditarPerfil
def editarPerfil(request):
    usuario = request.user 

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.password1 = informacion['password1']
            usuario.password1 = informacion['password2']
            usuario.save()

            #return HttpResponseRedirect('/AppBiblioCine/login/')
            return render(request, 'AppBiblioCine/inicio.html')
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "AppBiblioCine/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})

#Avatar

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()

            return render(request, 'AppBiblioCine/inicio.html')
    else:
        miFormulario = AvatarFormulario()
    return render(request, 'AppBiblioCine/agregarAvatar.html', {'miFormulario':miFormulario})

###LIBROS

def libros(request):
    if request.method == "POST":
        miFormulario = LibroFormulario (request.POST, request.FILES)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            libro = Libro (titulo = informacion['titulo'], 
                                 autor=informacion['autor'], 
                                 año_publicacion=informacion['año_publicacion'], 
                                 editorial=informacion['editorial'],
                                 sinopsis=informacion['sinopsis'],
                                 genero=informacion['genero'],
                                 idioma=informacion['idioma'],
                                 portada=informacion['portada'],
                                 )
            libro.save()
            return render(request, 'AppBiblioCine/inicio.html') 
    else:
        miFormulario=LibroFormulario()
    return render (request, "AppBiblioCine/libros.html", {"miFormulario": miFormulario})

def comentarioLibros(request):
    if request.method == "POST":
        miFormulario = ComentarioLibroFormulario (request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            comentariolibro = ComentarioLibro (libro = informacion['libro'], 
                                 nombre=informacion['nombre'], 
                                 comentario=informacion['comentario'], 
                                 )
            comentariolibro.save()

            return render(request, 'AppBiblioCine/inicio.html')

    else:
        miFormulario=ComentarioLibroFormulario()
    return render (request, "AppBiblioCine/comentarioslibros.html", {"miFormulario": miFormulario})

#CRUD

#Busqueda

def busquedaAutor(request):
     return render(request, 'AppBiblioCine/busquedaAutor.html')

def buscar(request):
    if request.GET["autor"]:
          autor = request.GET['autor']
          libros = Libro.objects.filter(autor__icontains = autor)
          return render(request, 'AppBiblioCine/resultadosBusqueda.html', {'libros': libros, 'autor': autor})
    else:  
        respuesta="No enviaste datos"
            
    return render (request, "AppBiblioCine/inicio.html", {"respuesta": respuesta})

#Lectura

def leerLibros(request):
    libros = Libro.objects.all()
    contexto = {"libros":libros}
    return render(request, "AppBiblioCine/leerLibros.html", contexto)

def leerComentarioLibros(request):
    comentarios = ComentarioLibro.objects.all()
    contexto = {"comentarios":comentarios}
    print(comentarios)
    return render(request, "AppBiblioCine/leerComentariosLibros.html", contexto)

#Delete

def eliminarLibros (request, libro_titulo):
    libro = Libro.objects.get(titulo=libro_titulo)
    libro.delete()

    libros = Libro.objects.all()
    contexto = {"libros":libros}
    return render(request, "AppBiblioCine/leerLibros.html", contexto)

def eliminarComentarioLibros (request, comentario_comentario):
    comentario = ComentarioLibro.objects.get(comentario=comentario_comentario)
    comentario.delete()

    comentarios = ComentarioLibro.objects.all()
    contexto = {"comentarios":comentarios}
    return render(request, "AppBiblioCine/leerComentariosLibros.html", contexto)

#Edicion

def editarLibros(request, libro_titulo):
    libro = Libro.objects.get(titulo = libro_titulo)

    if  request.method == "POST":
        miFormulario = LibroFormulario (request.POST)
        print (miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            libro.titulo = informacion['titulo']
            libro.autor = informacion ['autor']
            libro.año_publicacion = informacion['año_publicacion']
            libro.editorial = informacion['editorial']
            libro.sinopsis = informacion['sinopsis']
            libro.genero = informacion['genero']
            libro.idioma = informacion['idioma']
            libro.portada = informacion['portada']

            libro.save()

            return render (request, 'AppBiblioCine/inicio.html')
        
    else:
            miFormulario = LibroFormulario(initial={'titulo': libro.titulo,
                                                       'autor': libro.autor,
                                                       'año_publicacion': libro.año_publicacion,
                                                       'editorial': libro.editorial,
                                                       'sinopsis': libro.sinopsis,
                                                       'genero': libro.genero,
                                                       'idioma': libro.idioma,
                                                       'portada': libro.portada})
                        
            
    return render (request, 'AppBiblioCine/editarLibro.html', {'miFormulario': miFormulario, 'libro_titulo': libro_titulo})

#Clases basadas en vistas

class LibroList(ListView):
    model = Libro
    template_name='AppBiblioCine/libroList.html'

class LibroDetalle (DetailView):
    model = Libro
    template_name='AppBiblioCine/libroDetalle.html'

class LibroCreacion (CreateView):
    model = Libro
    success_url='AppBiblioCine/libro/list'
    fields = ['titulo', 'autor']

class LibroUpdate (UpdateView):
    model = Libro
    success_url = reverse_lazy('List')
    fields = ['titulo', 'autor']

class LibroDelete (DeleteView):
    model = Libro
    success_url = reverse_lazy('List')

###PELICULAS

def peliculas(request):
    if request.method == "POST":
        miFormulario = PeliculaFormulario (request.POST, request.FILES)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            pelicula = Pelicula (titulo = informacion['titulo'], 
                                 director=informacion['director'], 
                                 año_lanzamiento=informacion['año_lanzamiento'],
                                 sinopsis=informacion['sinopsis'], 
                                 genero=informacion['genero'],
                                 duracion=informacion['duracion'],
                                 portada=informacion['portada'],
                                 )
            pelicula.save()
            return render(request, 'AppBiblioCine/inicio.html') 
    else:
        miFormulario=PeliculaFormulario()
    return render (request, "AppBiblioCine/peliculas.html", {"miFormulario": miFormulario})
