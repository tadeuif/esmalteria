from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=250)
    tipo = models.CharField(max_length=250)
    marca = models.CharField(max_length=250)
    cor = models.CharField(max_length=250)
    qtd_disponivel = models.IntegerField(default=0)
    qtd_min_disponivel = models.IntegerField(default=0)
    pco_custo = models.FloatField()
    pco_venda = models.FloatField()
    dt_ultima_compra = models.DateField(default='1900-01-01')



    def __str__(self):
        return self.nome