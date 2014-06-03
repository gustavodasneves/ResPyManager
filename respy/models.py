from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#teste DVCS

class Turno (models.Model):
    turno_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    inicio = models.TimeField()

    def __unicode__(self):
        return self.nome

class HorarioPeriodo (models.Model):
    periodo_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    turno_id = models.ForeignKey(Turno)
    inicio = models.TimeField()
    termino = models.TimeField()

class Local (models.Model):
    local_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    disponivel = models.BooleanField()

class Ambiente (models.Model):
    ambiente_id = models.AutoField(primary_key=True)
    local_id = models.ForeignKey(Local)
    nome = models.CharField(max_length=100)
    disponivel = models.BooleanField()

class HorarioAmbiente (models.Model):
    horarioambiente_id = models.AutoField(primary_key=True)
    ambiente_id = models.ForeignKey(Ambiente)
    periodo_id = models.ForeignKey(HorarioPeriodo)

class Agendamento (models.Model):
    agendamento_id = models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User)
    ambiente_id = models.ForeignKey(Ambiente)
    datacadastro = models.DateField()
    datainicio = models.DateField()
    datafim = models.DateField()

class AgendaAmbiente (models.Model):
    agendaambiente_id = models.AutoField(primary_key=True)
    agendamento_id = models.ForeignKey(Agendamento)
    horarioambiente_id = models.ForeignKey(HorarioAmbiente)

class Equipamento (models.Model):
    equipamento_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    disponivel = models.BooleanField()

class AgendaEquipamento (models.Model):
    agendaequipamento_id = models.AutoField(primary_key=True)
    agendamento_id = models.ForeignKey(Agendamento)
    equipamento_id = models.ForeignKey(Equipamento)
    horarioambiente_id = models.ForeignKey(HorarioAmbiente)



