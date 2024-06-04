from django.db import models

# Create your models here.
class editorial(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='nombre', null=True)

    def __str__(self):
        fila = self.nombre
        return fila

class autor(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='nombre', null=True)
    apellido = models.CharField(max_length=20, verbose_name='apellido', null=True)
    nacionalidad = models.CharField(max_length=20, verbose_name='nacionalidad', null=True)

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "Nacionalidad: " + self.nacionalidad
        return fila
    


class libro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    precio = models.CharField(max_length=50, verbose_name='Precio')
    descripcion = models.TextField(verbose_name='Descripcion', null=True)
    autor = models.ForeignKey(autor, null=True, blank=True, on_delete=models.CASCADE)
    editorial = models.ForeignKey(editorial, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "Descripcion: " + self.descripcion
        return fila

class cliente(models.Model):
    cedula = models.CharField(max_length=20, verbose_name='cedula', null=True)
    libro = models.ForeignKey(libro, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    email = models.CharField(max_length=100, verbose_name='Email')

    def __str__(self):
        fila = "Nombre : " + self.nombre + " - " + "Email : " + self.email + " - " + "cedula : " + self.cedula
        return fila

   




    


