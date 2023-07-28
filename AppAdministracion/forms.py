from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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

#Avatar

class AvatarFormulario(forms.Form):
    #especificar los campos
    username=forms.ModelChoiceField(queryset=User.objects.all())
    imagen = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ['imagen']
        help_texts = {k:"" for k in fields}


