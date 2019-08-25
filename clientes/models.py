from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=250)
    sobrenome = models.CharField(max_length=250)
    email = models.EmailField()
    cpf = models.CharField(max_length=14,unique=True)
    dt_nascimento = models.DateField(default='1900-01-01')
    celular = models.CharField(max_length=15)
    redes = models.CharField(max_length=80)
    data_criacao = models.DateField(auto_now_add=True)



    def __str__(self):
        return self.nome