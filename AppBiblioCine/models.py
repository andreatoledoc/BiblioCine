from django.db import models

#Peliculas

class Pelicula (models.Model):
    titulo = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    genero = models.CharField(max_length=150)
    año_lanzamiento = models.IntegerField()
    duracion = models.IntegerField()
    sinopsis = models.TextField()
    portada = models.ImageField(upload_to='peliculas/')

class ComentarioPelicula(models.Model):
    comentario = models.ForeignKey(Pelicula, related_name='comentariosPeliculas', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)

#Libros

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    año_publicacion = models.IntegerField()
    editorial = models.CharField(max_length=100)
    sinopsis = models.TextField()
    genero = models.CharField(max_length=50)
    idioma = models.CharField(max_length=50)
    portada = models.ImageField(upload_to='libros/')

class ComentarioLibro(models.Model):
    comentario = models.ForeignKey(Pelicula, related_name='comentariosLibros', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)




