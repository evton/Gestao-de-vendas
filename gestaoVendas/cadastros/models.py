from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=250)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    loja = models.IntegerField()
    localizacao = models.CharField(max_length=50, verbose_name='Localização')

    def __str__(self):
        return "{} - loja {} - {}".format(self.nome, self.loja, self.localizacao)