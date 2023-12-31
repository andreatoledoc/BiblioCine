# Generated by Django 4.2.2 on 2023-07-28 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppBiblioCine', '0007_alter_comentariolibro_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentariopelicula',
            name='mensaje',
        ),
        migrations.AddField(
            model_name='comentariopelicula',
            name='pelicula',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentariosPeliculas', to='AppBiblioCine.pelicula'),
        ),
        migrations.AddField(
            model_name='libro',
            name='recomendacion',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='recomendacion',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='comentariopelicula',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comentariopelicula',
            name='nombre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='nombre'),
        ),
    ]
