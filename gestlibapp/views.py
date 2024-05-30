from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import libro
from .forms import LibroForm

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar(request, id):
    libros = libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libros)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminar(request, id):
    libros = libro.objects.get(id=id)
    libros.delete()
    return redirect('libros')

def catalogo(request):
    return render(request, 'catalogo/catalogo.html')

def comprar(request):
    return render(request, 'catalogo/comprar.html')
