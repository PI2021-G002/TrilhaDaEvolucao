from typing_extensions import Annotated
from django.db import models

class Voluntario(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    disponibilidade = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class AreaVoluntario(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

        
    
class AreaAtuacaoVoluntario(models.Model):
    id_vol = models.ForeignKey(
       Voluntario,
       on_delete=models.DO_NOTHING
    )
    id_area_vol = models.ForeignKey(
       AreaVoluntario,
       on_delete=models.DO_NOTHING
    )
    descricao = models.CharField(max_length=1000)
    
class Familia(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    ano = models.IntegerField()
    nro_membros = models.IntegerField()
    acomp_concluido = models.BooleanField(default=False)
    def __str__(self):
        return self.nome

class AreaPrograma(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)
    def __str__(self):
        return self.nome

class AreaAcompanhamento(models.Model):
    id_familia = models.ForeignKey(
       Familia,
       on_delete=models.DO_NOTHING
    )
    id_area_programa = models.ForeignKey(
       AreaPrograma,
       on_delete=models.DO_NOTHING
    )
    concluido = models.BooleanField(default=False)
    data_inicio = models.DateField(auto_now=False, auto_now_add=True) 
    data_termino = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    observacao =  models.CharField(max_length=255)
    completude = models.FloatField(null=True,blank=True)

class Agendamentos(models.Model):
    data = models.DateField(auto_now=False, auto_now_add=False)
    hora = models.TimeField(auto_now=False, auto_now_add=False, null=True )
    id_familia = models.ForeignKey(
       Familia,
       on_delete=models.DO_NOTHING
    )
    tipo = models.CharField(max_length=1)
    id_tipo = models.BigIntegerField() 
    
    @property
    def get_volparcprog_name(self):
        if self.tipo == "V":
          temp = Voluntario.objects.filter(id=self.id_tipo).values('nome').last()
          return str("Com Volunt??rio " + temp['nome'])
        
        if self.tipo == "R":
          temp = Parceiro.objects.filter(id=self.id_tipo).values('nome').last()
          return str("Com Parceiro " + temp['nome'])
 
        if self.tipo == "P":
            temp = AreaPrograma.objects.filter(id=self.id_tipo).values('nome').last()
            return str("Programa " + temp['nome'])
        return str("") 

class Parceiro(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    disponibilidade = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class AreaParceiro(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class AreaAtuacaoParceiro(models.Model):
    id_par = models.ForeignKey(
       Parceiro,
       on_delete=models.DO_NOTHING
    )
    id_area_par = models.ForeignKey(
       AreaParceiro,
       on_delete=models.DO_NOTHING
    )
    descricao = models.CharField(max_length=1000)