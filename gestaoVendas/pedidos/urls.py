from django.urls import path
from . import views

urlpatterns = [
    path('pedidos/', views.listapedidos, name='pedidos'),
    path('novopedido/', views.novopedido, name='novopedido')
]