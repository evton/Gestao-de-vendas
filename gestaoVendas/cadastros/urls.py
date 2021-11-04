from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.ClienteCreate.as_view(), name='cadastroCliente'),
]