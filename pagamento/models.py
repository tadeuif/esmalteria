from django.db import models
from clientes.models import Cliente
from servicos.models import Servico

# Create your models here.
class Pagamento(models.Model):
    #id_pagamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    cod_servico = models.ForeignKey('servicos.Servico',on_delete=models.CASCADE)
    cod_cliente = models.ForeignKey('clientes.Cliente',on_delete=models.CASCADE)
    valor_pagamento = models.FloatField()
    dt_pagamento = models.DateField(default='1900-01-01')
    status = models.CharField(max_length=10, default='Aberto')

    def __str__(self):
        return self.nome