from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.utils.text import Truncator, slugify

class User(AbstractUser):
    pass

class Categoria(models.Model):
    nombre = models.CharField(_('Nombre'), max_length=120, unique=True)
    slug = models.SlugField(_('Slug'), max_length=120, unique=True)
    activa = models.BooleanField(_('Activa'), default=True)
    creada = models.DateTimeField(_('Creada'), auto_now_add=True)

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
    nombre = models.CharField(_('Nombre'), max_length=120)
    descripcion = models.TextField(_('Descripcion'), null=True, blank=True)
    imagen = models.ImageField(_('Imagen'), upload_to='imagen_curso')
    creado = models.DateTimeField(_('Creado'), auto_now_add=True)
    actualizado = models.DateTimeField(_('Actualizado'), auto_now=True)
    link = models.URLField(_('Link'), max_length=300)
    precio = models.DecimalField(_('Precio'), max_digits=6,
                              decimal_places=2)
    
    activo = models.BooleanField(_('Activo'), default=True)
    promocion = models.CharField(_('Promocion'), max_length=100, null=True, blank=True)

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
    src = models.FileField(_('Imagen'), upload_to='hero')

    class Meta:
        verbose_name = 'Logo'
        # plural_verbose_name = 'Logo'