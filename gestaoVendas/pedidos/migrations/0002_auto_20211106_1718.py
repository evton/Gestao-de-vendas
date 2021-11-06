# Generated by Django 3.2.9 on 2021-11-06 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(blank=True, default='', max_length=3000, null=True)),
                ('pedido_numero', models.IntegerField(blank=True, null=True)),
                ('pedido_data', models.DateField(blank=True, null=True)),
                ('produto1', models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='produto 1')),
                ('produto1_quantidade', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantidade')),
                ('produto1_preco', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Preço')),
                ('produto1_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Total')),
                ('produto2', models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='produto 2')),
                ('produto2_quantidade', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantidade')),
                ('produto2_preco', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Preço')),
                ('produto2_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Total')),
                ('produto3', models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='produto 3')),
                ('produto3_quantidade', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantidade')),
                ('produto3_preco', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Preço')),
                ('produto3_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Total')),
                ('produto4', models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='produto 4')),
                ('produto4_quantidade', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantidade')),
                ('produto4_preco', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Preço')),
                ('produto4_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Total')),
                ('produto5', models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='produto 5')),
                ('produto5_quantidade', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantidade')),
                ('produto5_preco', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Preço')),
                ('produto5_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Total')),
                ('telefone', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Total')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('pago', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Nota',
        ),
    ]
