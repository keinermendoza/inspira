from collections.abc import Iterable
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.utils.text import Truncator, slugify

class User(AbstractUser):
    pass

class Categoria(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    activa = models.BooleanField(default=True)
    creada = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nombre
    
    def save(self):
        self.slug = slugify(self.nombre)
        return super().save()
    
class Voto(models.Model):
    puntos = models.IntegerField(validators=[
                                         MinValueValidator(1),
                                         MaxValueValidator(5)
                                     ])
    def __str__(self) -> str:
        return f"Valoracion de {self.puntos} puntos"

class Curso(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='imagen_curso')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    link = models.URLField(max_length=300)
    precio = models.DecimalField(max_digits=6,
                              decimal_places=2)
    
    activo = models.BooleanField(default=True)
    promocion = models.CharField(max_length=100, null=True, blank=True)

    categoria = models.ForeignKey(Categoria, related_name='cursos',
                                  on_delete=models.PROTECT)
    
    ranking = models.ManyToManyField(Voto, related_name='curso', null=True, blank=True)


    def __str__(self) -> str:
        return f"Curos: {self.nombre}"
    
    @property
    def short_descripcion(self):
        return Truncator(self.descripcion).words(7)
    
    
    class Meta:
        ordering = ["creado"]
        indexes = [
            models.Index(fields=["creado"])
        ]

# this will be for temporal use
class HeroImg(models.Model):
    src = models.FileField(upload_to='hero')