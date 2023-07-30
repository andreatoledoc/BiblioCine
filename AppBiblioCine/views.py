from django.shortcuts import render, redirect
from AppBiblioCine.models import Libro, Pelicula, ComentarioLibro, ComentarioPelicula
from django.http import HttpResponse
from AppBiblioCine.forms import LibroFormulario, PeliculaFormulario, ComentarioLibroFormulario, ComentarioPeliculaFormulario
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
                                 recomendacion=informacion['recomendacion'],
                                 )
            libro.save()
            return render(request, 'AppAdministracion/inicio.html') 
    else:
        miFormulario=LibroFormulario()
    return render (request, "AppBiblioCine/libros.html", {"miFormulario": miFormulario})

@login_required
def comentarioLibros(request, id):

    comentario = ComentarioLibroFormulario.objects.filter(libro__id=id)

    if request.method == "POST":
        miFormulario = ComentarioLibroFormulario (request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            comentariolibro = ComentarioLibro (libro = request.libro, 
                                 nombre=request.user, 
                                 comentario=informacion['comentario'], 
                                 )
            comentariolibro.save()

            return render(request, 'AppAdministracion/inicio.html')

    else:
        miFormulario=ComentarioLibroFormulario()
    return render (request, "AppBiblioCine/comentariosLibros.html", {"miFormulario": miFormulario})

#CRUD

#Busqueda

def busquedaLibro(request):
     return render(request, 'AppBiblioCine/busquedaLibro.html')

def buscarLibro(request):
    campo = request.GET.get("campo")
    termino = request.GET.get("termino")

    if campo and termino:
        if campo == "autor":
            libros = Libro.objects.filter(autor__icontains=termino)
        elif campo == "titulo":
            libros = Libro.objects.filter(titulo__icontains=termino)
        elif campo == "genero":
            libros = Libro.objects.filter(genero__icontains=termino)
        else:
            libros = []
    else:
        libros = []

    return render(request, 'AppBiblioCine/resultadosBusquedaLibro.html', {'libros': libros, 'termino': termino, 'campo': campo})

#Lectura

def leerLibros(request):
    libros = Libro.objects.all()
    contexto = {"libros":libros}
    return render(request, "AppBiblioCine/leerLibros.html", contexto)

def leerComentarioLibros(request, id):
    comentarios = ComentarioLibro.objects.all()
    comentarios = ComentarioLibro.objects.filter(libro__id=id)

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
        miFormulario = LibroFormulario (request.POST, request.FILES)
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
            libro.recomendacion = informacion['recomendacion']

            libro.save()

            return render (request, 'AppAdministracion/inicio.html')
        
    else:
            miFormulario = LibroFormulario(initial={'titulo': libro.titulo,
                                                       'autor': libro.autor,
                                                       'año_publicacion': libro.año_publicacion,
                                                       'editorial': libro.editorial,
                                                       'sinopsis': libro.sinopsis,
                                                       'genero': libro.genero,
                                                       'idioma': libro.idioma,
                                                       'portada': libro.portada,
                                                       'recomendacion': libro.recomendacion})
                        
            
    return render (request, 'AppBiblioCine/editarLibro.html', {'miFormulario': miFormulario, 'libro_titulo': libro_titulo})

def editarComentarioLibros(request, comentario_comentario):
    comentario = ComentarioLibro.objects.get(comentario = comentario_comentario)

    if  request.method == "POST":
        miFormulario = ComentarioLibroFormulario (request.POST)
        print (miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            comentario.comentario = informacion['comentario']
            comentario.save()

            return render (request, 'AppAdministracion/inicio.html')
        
    else:
            miFormulario = ComentarioLibroFormulario(initial={'comentario': comentario.comentario})
                                    
    return render (request, 'AppBiblioCine/editarComentarioLibro.html', {'miFormulario': miFormulario, 'comentario_comentario': comentario_comentario})


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
                                 recomendacion=informacion['recomendacion'],
                                 )
            pelicula.save()
            return render(request, 'AppAdministracion/inicio.html') 
    else:
        miFormulario=PeliculaFormulario()
    return render (request, "AppBiblioCine/peliculas.html", {"miFormulario": miFormulario})

@login_required
def comentarioPeliculas(request):
    if request.method == "POST":
        miFormulario = ComentarioPeliculaFormulario (request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            comentariopelicula = ComentarioPelicula (pelicula = informacion['pelicula'], 
                                 nombre=request.user, 
                                 comentario=informacion['comentario'], 
                                 )
            comentariopelicula.save()

            return render(request, 'AppAdministracion/inicio.html')

    else:
        miFormulario=ComentarioPeliculaFormulario()
    return render (request, "AppBiblioCine/comentariosPeliculas.html", {"miFormulario": miFormulario})

#CRUD

#Busqueda

def busquedaPelicula(request):
     return render(request, 'AppBiblioCine/busquedaPelicula.html')

def buscarPelicula(request):
    campo = request.GET.get("campo")
    termino = request.GET.get("termino")

    if campo and termino:
        if campo == "director":
            peliculas = Pelicula.objects.filter(director__icontains=termino)
        elif campo == "titulo":
            peliculas = Pelicula.objects.filter(titulo__icontains=termino)
        elif campo == "genero":
            peliculas = Pelicula.objects.filter(genero__icontains=termino)
        else:
            peliculas = []
    else:
        peliculas = []

    return render(request, 'AppBiblioCine/resultadosBusquedaPelicula.html', {'peliculas': peliculas, 'termino': termino, 'campo': campo})

#Lectura

def leerPeliculas(request):
    peliculas = Pelicula.objects.all()
    contexto = {"peliculas":peliculas}
    return render(request, "AppBiblioCine/leerPeliculas.html", contexto)

def leerComentarioPeliculas(request):
    comentarios = ComentarioPelicula.objects.all()
    comentarios = ComentarioPelicula.objects.filter(pelicula__id = id)

    contexto = {"comentarios":comentarios}
    print(comentarios)
    return render(request, "AppBiblioCine/leerComentariosPeliculas.html", contexto)

#Delete

def eliminarPeliculas (request, pelicula_titulo):
    pelicula = Pelicula.objects.get(titulo=pelicula_titulo)
    pelicula.delete()

    peliculas = Pelicula.objects.all()
    contexto = {"peliculas":peliculas}
    return render(request, "AppBiblioCine/leerPeliculas.html", contexto)

def eliminarComentarioPeliculas (request, comentario_comentario):
    comentario = ComentarioPelicula.objects.get(comentario=comentario_comentario)
    comentario.delete()

    comentarios = ComentarioPelicula.objects.all()
    contexto = {"comentarios":comentarios}
    return render(request, "AppBiblioCine/leerComentariosPeliculas.html", contexto)


#Edicion

def editarPeliculas(request, pelicula_titulo):
    pelicula = Pelicula.objects.get(titulo = pelicula_titulo)

    if  request.method == "POST":
        miFormulario = PeliculaFormulario (request.POST, request.FILES)
        print (miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            pelicula.titulo = informacion['titulo']
            pelicula.director = informacion ['director']
            pelicula.año_lanzamiento = informacion['año_lanzamiento']
            pelicula.sinopsis = informacion['sinopsis']
            pelicula.genero = informacion['genero']
            pelicula.duracion = informacion['duracion']
            pelicula.portada = informacion['portada']
            pelicula.recomendacion = informacion['recomendacion']

            pelicula.save()

            return render (request, 'AppAdministracion/inicio.html')
        
    else:
            miFormulario = PeliculaFormulario(initial={'titulo': pelicula.titulo,
                                                       'director': pelicula.director,
                                                       'año_lanzamiento': pelicula.año_lanzamiento,
                                                       'sinopsis': pelicula.sinopsis,
                                                       'genero': pelicula.genero,
                                                       'duracion': pelicula.duracion,
                                                       'portada': pelicula.portada,
                                                       'recomendacion': pelicula.recomendacion})
                        
            
    return render (request, 'AppBiblioCine/editarPelicula.html', {'miFormulario': miFormulario, 'pelicula_titulo': pelicula_titulo})


def editarComentarioPeliculas(request, comentario_comentario):
    comentario = ComentarioPelicula.objects.get(comentario = comentario_comentario)

    if  request.method == "POST":
        miFormulario = ComentarioPeliculaFormulario (request.POST)
        print (miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            comentario.comentario = informacion['comentario']
            comentario.save()

            return render (request, 'AppAdministracion/inicio.html')
        
    else:
            miFormulario = ComentarioPeliculaFormulario(initial={'comentario': comentario.comentario})
                                    
    return render (request, 'AppBiblioCine/editarComentarioPelicula.html', {'miFormulario': miFormulario, 'comentario_comentario': comentario_comentario})


#Clases basadas en vistas

class PeliculaList(ListView):
    model = Pelicula
    template_name='AppBiblioCine/peliculaList.html'

class PeliculaDetalle (DetailView):
    model = Pelicula
    template_name='AppBiblioCine/peliculaDetalle.html'

class PeliculaCreacion (CreateView):
    model = Pelicula
    success_url='AppBiblioCine/pelicula/list'
    fields = ['titulo', 'director']

class PeliculaUpdate (UpdateView):
    model = Pelicula
    success_url = reverse_lazy('List')
    fields = ['titulo', 'director']

class PeliculaDelete (DeleteView):
    model = Pelicula
    success_url = reverse_lazy('List')