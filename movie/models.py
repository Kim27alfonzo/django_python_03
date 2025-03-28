
from django.db import models

class Pelicula(models.Model):
    GENRE_CHOICES = [
        ('action', 'Acción'),
        ('comedy', 'Comedia'),
        ('drama', 'Drama'),
        ('fantasy', 'Fantasía'),
        ('horror', 'Terror'),
        ('romance', 'Romance'),
        ('sci-fi', 'Ciencia Ficción'),
        ('thriller', 'Thriller'),
        ('western', 'Western'),
        ('other', 'Otro'),
    ]


    nombre = models.CharField(max_length=200, verbose_name="Nombre de la película")
    autor = models.CharField(max_length=100, verbose_name="Director/Autor")
    descripcion = models.TextField(verbose_name="Descripción")
    descripcion_ampliada = models.TextField(verbose_name="Descripción ampliada", blank=True, null=True)  # Nuevo campo
    duracion_minutos = models.PositiveIntegerField(verbose_name="Duración (minutos)")
    genero = models.CharField(max_length=100, verbose_name="Género")
    portada = models.ImageField(upload_to='portadas/', verbose_name="Portada", null=True, blank=True)

    def __str__(self):
        return self.nombre