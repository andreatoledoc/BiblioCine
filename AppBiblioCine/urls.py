from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from AppBiblioCine import views

urlpatterns = [
    path('libros/', views.libros, name='Libros'),
    path('comentarioLibros/<id>', views.comentarioLibros, name='ComentarioLibros'),
    #path('libroFormulario/', views.libroFormulario, name='LibroFormulario'),

    path('peliculas/', views.peliculas, name='Peliculas'),
    path('comentarioPeliculas/<id>', views.comentarioPeliculas, name='ComentarioPeliculas'),
    #path('peliculaFormulario/', views.peliculaFormulario, name='PeliculaFormulario'),
    
    path('busquedaLibro/', views.busquedaLibro, name='BusquedaLibro'),
    path('buscarLibro/', views.buscarLibro, name="BuscarLibro"),

    path('busquedaPelicula/', views.busquedaPelicula, name='BusquedaPelicula'),
    path('buscarPelicula/', views.buscarPelicula, name="BuscarPelicula"),

    path('ver-libro/<int:id>/', views.verLibro, name='VerLibro'),
    path('ver-pelicula/<int:id>/', views.verPelicula, name='VerPelicula'),

    path( 'leerLibros/', views.leerLibros, name='LeerLibros'),
    path( 'leerPeliculas/', views.leerPeliculas, name='LeerPeliculas'),

    path ( 'eliminarLibros/<libro_titulo>', views.eliminarLibros, name='EliminarLibros'),
    path ( 'eliminarPeliculas/<pelicula_titulo>', views.eliminarPeliculas, name='EliminarPeliculas'),

    path ( 'editarLibros/<libro_titulo>', views.editarLibros, name='EditarLibros'),
    path ( 'editarPeliculas/<pelicula_titulo>', views.editarPeliculas, name='EditarPeliculas'),

    path( 'leerComentarioLibros/<id>', views.leerComentarioLibros, name='LeerComentarioLibros'),
    path( 'leerComentarioPeliculas/<id>', views.leerComentarioPeliculas, name='LeerComentarioPeliculas'),

    path ( 'eliminarComentarioLibros/<comentario_comentario>', views.eliminarComentarioLibros, name='EliminarComentarioLibros'),
    path ( 'eliminarComentarioPeliculas/<comentario_comentario>', views.eliminarComentarioPeliculas, name='EliminarComentarioPeliculas'),
    
    path ( 'editarComentarioLibros/<comentario_comentario>', views.editarComentarioLibros, name='EditarComentarioLibros'),
    path ( 'editarComentarioPeliculas/<comentario_comentario>', views.editarComentarioPeliculas, name='EditarComentarioPeliculas'),

    path ('libro/list', views.LibroList.as_view(), name='ListLibros'),
    path ('libro/detail/<pk>', views.LibroDetalle.as_view(), name='DetailLibros'),
    path (r'^nuevo$', views.LibroCreacion.as_view(), name='NewLibro'),
    path (r'^editar/(?P<pk>\d+)$', views.LibroUpdate.as_view(), name='EditLibros'),
    path (r'^borrar/(?P<pk>\d+)$', views.LibroDelete.as_view(), name='DeleteLibros'),

    path ('pelicula/list', views.PeliculaList.as_view(), name='ListPeliculas'),
    path ('pelicula/detail/<pk>', views.PeliculaDetalle.as_view(), name='DetailPeliculas'),
    path (r'^nuevo$', views.PeliculaCreacion.as_view(), name='NewPelicula'),
    path (r'^editar/(?P<pk>\d+)$', views.PeliculaUpdate.as_view(), name='EditPeliculas'),
    path (r'^borrar/(?P<pk>\d+)$', views.PeliculaDelete.as_view(), name='DeletePeliculas'),
]
