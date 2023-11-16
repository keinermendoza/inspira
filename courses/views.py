from django.shortcuts import render
from .models import Curso, Categoria


def home(request):
    context = {
        'sections':Categoria.objects.all()
    }
    return render(request, 'courses/home.html', context)