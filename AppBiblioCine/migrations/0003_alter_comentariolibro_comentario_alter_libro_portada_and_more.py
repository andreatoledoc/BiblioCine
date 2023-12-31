# Generated by Django 4.2.2 on 2023-07-23 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppBiblioCine', '0002_comentariopelicula_comentariolibro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentariolibro',
            name='comentario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentariosLibros', to='AppBiblioCine.libro'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='portada',
            field=models.ImageField(upload_to='media/libros/'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='portada',
            field=models.ImageField(upload_to='media/peliculas/'),
        ),
    ]
