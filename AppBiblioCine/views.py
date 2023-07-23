from django.shortcuts import render
from AppBiblioCine.models import Libro, Pelicula, ComentarioLibro
from django.http import HttpResponse
from AppBiblioCine.forms import LibroFormulario, PeliculaFormulario, ComentarioLibroFormulario

#Inicio

def inicio(request):
    return render (request, "AppBiblioCine/inicio.html")

#Libros

def libros(request):
    if request.method == "POST":
        miFormulario = LibroFormulario (request.POST)
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

def leerLibros(request):
    libros = Libro.objects.all()
    contexto = {"libros":libros}
    return render(request, "AppBiblioCine/leerLibros.html", contexto)

#Peliculas

def peliculas(request):
    return render (request, "AppBiblioCine/peliculas.html")

def peliculas(request):
    if request.method == "POST":
        miFormulario = PeliculaFormulario (request.POST)
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

