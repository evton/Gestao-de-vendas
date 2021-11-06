from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.novocliente, name='cadastrocliente'),
]