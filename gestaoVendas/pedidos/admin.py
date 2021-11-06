from django.contrib import admin
from .models import Pedido
from .forms import Pedidoform

# Register your models here.
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido_numero', 'pedido_data']
    form = Pedidoform
    list_filter = ['pedido_numero']
    search_fields = ['pedido_numero', 'pedido_data']

admin.site.register(Pedido, PedidoAdmin)