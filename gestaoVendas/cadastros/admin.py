from django.contrib import admin
from .models import Cliente
from .forms import Clienteform

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'localizacao', 'loja']
    form = Clienteform
    list_filter = ['nome']
    search_fields = ['nome', 'localizacao', 'loja']

admin.site.register(Cliente, ClienteAdmin)