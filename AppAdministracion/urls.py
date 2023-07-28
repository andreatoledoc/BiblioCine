from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from AppAdministracion import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path( 'login', views.login_request, name='Login'),
    path ('register', views.register, name = "Register"),
    path ('logout', LogoutView.as_view (template_name='AppAdministracion/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    path('agregarAvatar', views.agregarAvatar, name='AgregarAvatar'),
    path('aboutMe', views.aboutMe, name='AboutMe'),
]