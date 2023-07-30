from django.shortcuts import render, redirect
from AppAdministracion.models import  Avatar
from django.http import HttpResponse
from AppAdministracion.forms import AvatarFormulario, UserEditForm, UserRegisterForm
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
from django.template import Template, Context
from django.template import loader

#Inicio
@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    print (avatares)
    return render(request, 'AppAdministracion/inicio.html', {'url':avatares[0].imagen.url, 'messages': messages.get_messages(request)})


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

                # Obtener el avatar del usuario si existe
                avatar_url = None
                avatares = Avatar.objects.filter(user=user)
                if avatares.exists():
                    avatar_url = avatares[0].imagen.url
                    
                return render (request, 'AppAdministracion/inicio.html', {'mensaje': f"Bienvenido {usuario}", 'user': user, 'login_success': True})

            else:
                return render(request, 'AppAdministracion/inicio.html', {"mensaje": "Error, datos erroneos", 'login_success': False})
        else:
            return render(request, 'AppAdministracion/inicio.html', {'mensaje': 'Error, formulario erroneo', 'form': form, 'login_success': False})
    
    form = AuthenticationForm()

    return render (request, 'AppAdministracion/login.html', {'form': form})

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

    return render (request, "AppAdministracion/registro.html", {"form":form})

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
            return render(request, 'AppAdministracion/inicio.html')
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "AppAdministracion/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})

#Avatar

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()

            return render(request, 'AppAdministracion/inicio.html')
    else:
        miFormulario = AvatarFormulario()
    return render(request, 'AppAdministracion/agregarAvatar.html', {'miFormulario':miFormulario})

#AboutMe

def aboutMe(request):
     return render(request, 'AppAdministracion/aboutMe.html')