from django.db import models

# Create your models here.
class Agendamentos(models.Model):
    data_hora = models.DateTimeField()
    tipo = models.CharField(max_length=1)
    id_tipo = models.BigIntegerField()
    def __str__(self):
        return self.nome