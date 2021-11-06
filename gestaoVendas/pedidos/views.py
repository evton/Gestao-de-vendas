from django.shortcuts import render, redirect
from .forms import Pedidoform
from .models import Pedido

# Create your views here.
def novopedido(request):
    form = Pedidoform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/pedidos')
    context = {
        "form": form,
    }
    return render(request, 'pedidos/novopedido.html', context)

def listapedidos(request):
    queryset = Pedido.objects.all()
    context = {
        "queryset": queryset,
    }
    return render(request, 'pedidos/pedidos.html', context)