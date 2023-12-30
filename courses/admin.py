from django import forms
from django.contrib import admin
from .models import Curso, Voto, Categoria, User, HeroImg

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'imagen', 'link', 'precio', 'promocion']

class CursoInlineAdmin(admin.StackedInline):
    model =  Curso
    form = CursoForm
    extra = 1

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
    list_display = ["nombre", "activa"]
    inlines = [CursoInlineAdmin]

admin.site.register(Voto)
admin.site.register(HeroImg)
