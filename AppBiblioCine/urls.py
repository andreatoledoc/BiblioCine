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
    path ( 'eliminarLibros/<libro_titulo>', views.eliminarLibros, name='EliminarLibros'),
    path ( 'editarLibros/<libro_titulo>', views.editarLibros, name='EditarLibros'),
    path( 'leerComentarioLibros/', views.leerComentarioLibros, name='LeerComentarioLibros'),
    path ( 'eliminarComentarioLibros/<comentario_comentario>', views.eliminarComentarioLibros, name='EliminarComentarioLibros'),
    path ('libro/list', views.LibroList.as_view(), name='List'),
    path (r'^(?P<pk>\d+)$', views.LibroDetalle.as_view(), name='Detail'),
    path (r'^nuevo$', views.LibroCreacion.as_view(), name='New'),
    path (r'^editar/(?P<pk>\d+)$', views.LibroUpdate.as_view(), name='Edit'),
    path (r'^borrar/(?P<pk>\d+)$', views.LibroDelete.as_view(), name='Delete'),
    path( 'login', views.login_request, name='Login'),
]
