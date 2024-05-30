from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('libros/', views.libros, name='libros'),
    path('libros/crear/', views.crear, name='crear'),
    path('libros/editar/', views.editar, name='editar'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('libros/editar/<int:id>', views.editar, name='editar'),
    path('catalogo/comprar/', views.comprar, name='comprar'),

]