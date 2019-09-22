from django.db import models

# Create your models here.
class Agendamento(models.Model):
    nome = models.CharField(max_length=250)
    dt_agendamento = models.DateField(default='1900-01-01')
    hora_agendamento = models.TimeField(default='00:00:00')
    servico_prestado= models.CharField(max_length=250)

    def __str__(self):
        return self.nome