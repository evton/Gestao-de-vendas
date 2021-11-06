from django.db import models

# Create your models here.
class Pedido(models.Model):
    comentario = models.TextField(max_length=3000, default='', blank=True, null=True)
    pedido_numero = models.IntegerField(blank=True, null=True)
    pedido_data = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    produto1 = models.CharField ('produto 1', max_length=120, default='', blank=True, null=True)
    produto1_quantidade = models.IntegerField('Quantidade', default=0, blank=True, null=True)
    produto1_preco = models.DecimalField('Preço', default=0, max_digits=7, decimal_places=2, blank=True, null=True)
    produto1_total = models.DecimalField('Total', default=0, max_digits=7, decimal_places=2, blank=True, null=True)

    produto2 = models.CharField ('produto 2', max_length=120, default='', blank=True, null=True)
    produto2_quantidade = models.IntegerField('Quantidade', default=0, blank=True, null=True)
    produto2_preco = models.DecimalField('Preço', default=0, max_digits=7, decimal_places=2, blank=True, null=True)
    produto2_total = models.DecimalField('Total', default=0, max_digits=7, decimal_places=2, blank=True, null=True)

    produto3 = models.CharField ('produto 3', max_length=120, default='', blank=True, null=True)
    produto3_quantidade = models.IntegerField('Quantidade', default=0, blank=True, null=True)
    produto3_preco = models.DecimalField('Preço', default=0, max_digits=7, decimal_places=2, blank=True, null=True)
    produto3_total = models.DecimalField('Total', default=0, max_digits=7, decimal_places=2, blank=True, null=True)

    produto4 = models.CharField ('produto 4', max_length=120, default='', blank=True, null=True)
    produto4_quantidade = models.IntegerField('Quantidade', default=0, blank=True, null=True)
    produto4_preco = models.DecimalField('Preço', default=0, max_digits=7, decimal_places=2, blank=True, null=True)
    produto4_total = models.DecimalField('Total', default=0, max_digits=7, decimal_places=2, blank=True, null=True)

    produto5 = models.CharField ('produto 5', max_length=120, default='', blank=True, null=True)
    produto5_quantidade = models.IntegerField('Quantidade', default=0, blank=True, null=True)
    produto5_preco = models.DecimalField('Preço', default=0, max_digits=7, decimal_places=2, blank=True, null=True)
    produto5_total = models.DecimalField('Total', default=0, max_digits=7, decimal_places=2, blank=True, null=True)

    telefone = models.CharField(max_length=20, default='', blank=True, null=True)
    total = models.DecimalField('Total', default=0, max_digits=7, decimal_places=2, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)
    pago = models.BooleanField(default=False)
 
    def __str__(self):
	    return self.produto1 + ' - ' +  str(self.pedido_numero)