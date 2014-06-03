from django.contrib import admin

# Register your models here.
from respy.models import Agendamento, Turno, HorarioPeriodo

class TurnoAdmin(admin.ModelAdmin):
    fields = ('nome', 'inicio',)
    list_display = ('turno_id', 'nome', 'inicio', )

admin.site.register(Agendamento)
admin.site.register(Turno, TurnoAdmin)
admin.site.register(HorarioPeriodo)