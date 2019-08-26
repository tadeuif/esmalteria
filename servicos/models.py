from django.db import models

# Create your models here.
class Servico(models.Model):
    nome = models.CharField(max_length=250)
    tipo = models.CharField(max_length=250)
    descricao = models.CharField(max_length=250)
    preco = models.FloatField()
    produto = models.CharField(max_length=250)
    disponibilidade = models.BooleanField()
    tm_execucao = models.TimeField()



    def __str__(self):
        return self.nome