from django.contrib import admin
from .models import Curso, Voto, Categoria, User

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "categoria", "short_descripcion", "creado"]
    readonly_fields=('ranking', )


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('slug', )

admin.site.register(Voto)
