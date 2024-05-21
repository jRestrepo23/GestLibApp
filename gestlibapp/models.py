from django.db import models

# Create your models here.
class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    email = models.CharField(max_length=100, verbose_name='Email')