from django.contrib.auth.models import User
from django.db import models

class Local (models.Model):
    local_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nome


class Equipamento (models.Model):
    equipamento_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nome

class Funcionario (models.Model):
    funcionario_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nome

class Aluguel (models.Model):
    aluguel_id = models.AutoField(primary_key=True)
    local_id = models.ForeignKey(Local)
    equipamento_id = models.ForeignKey(Equipamento)
    funcionario_id = models.ForeignKey(Funcionario)
    datahorainicio = models.DateTimeField()
    datahorafim = models.DateTimeField()
    ativo = models.BooleanField()







