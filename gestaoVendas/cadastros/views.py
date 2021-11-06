from django.shortcuts import render, redirect
from .forms import Clienteform


# Create your views here.
def novocliente(request):
    form = Clienteform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/cadastro')
    context = {
        "form": form,
    }
    return render(request, 'cadastros/cliente_form.html', context)

