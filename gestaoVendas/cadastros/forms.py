from django import forms
from .models import Cliente

class Clienteform(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'loja', 'localizacao', 'whastapp', 'telegram', 'observacao']