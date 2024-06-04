from django.contrib import admin
from .models import cliente,libro,editorial,autor
# Register your models here.
admin.site.register(cliente)
admin.site.register(libro)
admin.site.register(editorial)
admin.site.register(autor)
