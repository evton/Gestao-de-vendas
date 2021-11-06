from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=250)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    loja = models.IntegerField(null=True, blank=True)
    whastapp = models.BooleanField(default=False)
    telegram = models.BooleanField(default=False)
    observacao = models.CharField(max_length=500, blank=True, null=True, verbose_name='Observação')
    localizacao_opc = (
        ('Asa Norte', 'Asa Norte'),
        ('Asa Sul', 'Asa Sul'),
        ('Asa Leste', 'Asa Leste'),
        ('Asa Oeste', 'Asa Oeste'),
        ('Feira', 'Feira'),
        ('Externo', 'Externo')
    )
    localizacao = models.CharField(max_length=50, verbose_name='Localização', default='Asa Norte', blank=True, null=True, choices=localizacao_opc)


    def __str__(self):
        return "{} - loja {} - {}".format(self.nome, self.loja, self.localizacao)