from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Libro)
admin.site.register(ComentarioLibro)
admin.site.register(Pelicula)
admin.site.register(ComentarioPelicula)

