from django.contrib import admin
from .models import Curso, Voto, Categoria, User

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "categoria", "short_descripcion", "creado"]
    readonly_fields=('ranking', )


admin.site.register(User)
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('slug', )

admin.site.register(Voto)
