from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from AppBiblioCine import views

urlpatterns = [
    path('libros/', views.libros, name='Libros'),
    path('comentarioLibros/', views.comentarioLibros, name='ComentarioLibros'),
    #path('libroFormulario/', views.libroFormulario, name='LibroFormulario'),

    path('peliculas/', views.peliculas, name='Peliculas'),
    path('comentarioPeliculas/', views.comentarioPeliculas, name='ComentarioPeliculas'),
    #path('peliculaFormulario/', views.peliculaFormulario, name='PeliculaFormulario'),
    
    path('busquedaLibro/', views.busquedaLibro, name='BusquedaLibro'),
    path('buscarLibro/', views.buscarLibro, name="BuscarLibro"),

    path('busquedaPelicula/', views.busquedaPelicula, name='BusquedaPelicula'),
    path('buscarPelicula/', views.buscarPelicula, name="BuscarPelicula"),

    path( 'leerLibros/', views.leerLibros, name='LeerLibros'),
    path( 'leerPeliculas/', views.leerPeliculas, name='LeerPeliculas'),

    path ( 'eliminarLibros/<libro_titulo>', views.eliminarLibros, name='EliminarLibros'),
    path ( 'eliminarPeliculas/<pelicula_titulo>', views.eliminarPeliculas, name='EliminarPeliculas'),

    path ( 'editarLibros/<libro_titulo>', views.editarLibros, name='EditarLibros'),
    path ( 'editarPeliculas/<pelicula_titulo>', views.editarPeliculas, name='EditarPeliculas'),

    path( 'leerComentarioLibros/', views.leerComentarioLibros, name='LeerComentarioLibros'),
    path ( 'eliminarComentarioLibros/<comentario_comentario>', views.eliminarComentarioLibros, name='EliminarComentarioLibros'),
    path ( 'editarComentarioLibros/<comentario_comentario>', views.editarComentarioLibros, name='EditarComentarioLibros'),
    path ('libro/list', views.LibroList.as_view(), name='List'),
    path (r'^(?P<pk>\d+)$', views.LibroDetalle.as_view(), name='Detail'),
    path (r'^nuevo$', views.LibroCreacion.as_view(), name='New'),
    path (r'^editar/(?P<pk>\d+)$', views.LibroUpdate.as_view(), name='Edit'),
    path (r'^borrar/(?P<pk>\d+)$', views.LibroDelete.as_view(), name='Delete'),
]