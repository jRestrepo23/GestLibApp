from django import forms
from .models import libro,cliente

class LibroForm(forms.ModelForm):
    class Meta:
        model = libro
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'
