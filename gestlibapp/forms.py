from django import forms
from .models import libro,cliente

class LibroForm(forms.ModelForm):
    class Meta:
        model = libro
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ('cedula', 'libro', 'nombre', 'apellido', 'email')

        widgets = {
            'cedula': forms.TextInput(),
            'libro': forms.Select(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(),
            'apellido': forms.TextInput(),
            'email': forms.TextInput()

        }
