from django.db import models

# Create your models here.
class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    email = models.CharField(max_length=100, verbose_name='Email')

class libro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    precio = models.CharField(max_length=50, verbose_name='Precio')
    descripcion = models.TextField(verbose_name='Descripcion', null=True)

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "Descripcion: " + self.descripcion
        return fila


