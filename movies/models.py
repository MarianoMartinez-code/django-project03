from django.db import models

# Create your models here.

class Pelicula(models.Model):
    # Opciones para el campo 'genero'
    GENERO_CHOICES = [
        ('ACC', 'Acción'),
        ('COM', 'Comedia'),
        ('DRM', 'Drama'),
        ('TER', 'Terror'),
        ('SCI', 'Ciencia Ficción'),
        ('ANM', 'Animación'),
        ('AVT', 'Aventura'),
        ('FAN', 'Fantasía'),
        ('DOC', 'Documental'),
        ('OTH', 'Otro'),
    ]

    titulo = models.CharField(max_length=255, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción", blank=True, null=True)
    año_lanzamiento = models.IntegerField(verbose_name="Año de Lanzamiento")
    genero = models.CharField(max_length=3, choices=GENERO_CHOICES, verbose_name="Género")
    duracion = models.IntegerField(verbose_name="Duración (minutos)")
    director = models.CharField(max_length=255, verbose_name="Director")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")
    imagen = models.ImageField(upload_to='peliculas/', verbose_name="Imagen", blank=True, null=True)

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo