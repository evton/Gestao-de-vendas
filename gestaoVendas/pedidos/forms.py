from django import forms
from .models import Pedido

class Pedidoform(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['produto1', 'produto1_quantidade', 'produto1_preco', 'produto1_total','produto2', 'produto2_quantidade', 'produto2_preco', 'produto2_total','produto3', 'produto3_quantidade', 'produto3_preco', 'produto3_total','produto4', 'produto4_quantidade', 'produto4_preco', 'produto4_total','produto5', 'produto5_quantidade', 'produto5_preco', 'produto5_total','pedido_data', 'pedido_numero', 'pago', 'total']