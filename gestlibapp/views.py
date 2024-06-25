from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import libro,cliente
from .forms import LibroForm,ClienteForm,CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

@login_required
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
    forms = ClienteForm(request.POST or None)
    if request.method == 'POST' and forms.is_valid():
        forms.save()
        return redirect('catalogo')
    return render(request, 'catalogo/comprar.html', {'formulario': forms})

def exit(request):
    logout(request)
    return redirect('inicio')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        
        if user_creation_form.is_valid():
            user_creation_form.save()
            
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            
            return redirect('inicio')
    
    return render(request, 'registration/register.html', data)
