from django.db import models
from django.contrib.auth.models import User

#Libros

class Libro(models.Model):

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    año_publicacion = models.IntegerField()
    editorial = models.CharField(max_length=100)
    sinopsis = models.TextField()
    genero = models.CharField(max_length=150)
    idioma = models.CharField(max_length=50)
    portada = models.ImageField(upload_to='libros/')
    recomendacion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor} - Género: {self.genero}"

class ComentarioLibro(models.Model):
    libro = models.ForeignKey(Libro, related_name='comentariosLibros', on_delete=models.CASCADE, null=True)
    nombre = models.ForeignKey(User,blank=False,null=True,on_delete=models.CASCADE, verbose_name="nombre")
    comentario = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)
    
    #Peliculas

class Pelicula (models.Model):
    titulo = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    año_lanzamiento = models.IntegerField()
    sinopsis = models.TextField()
    genero = models.CharField(max_length=150)
    duracion = models.IntegerField()
    portada = models.ImageField(upload_to='peliculas/')
    recomendacion = models.TextField(default=0)

    def __str__(self):
        return f"Titulo: {self.titulo} - Director: {self.director} - Género: {self.genero}"

class ComentarioPelicula(models.Model):
    pelicula = models.ForeignKey(Pelicula, related_name='comentariosPeliculas', on_delete=models.CASCADE, null=True)
    nombre = models.ForeignKey(User,blank=False,null=True,on_delete=models.CASCADE, verbose_name="nombre")
    comentario = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)
    









