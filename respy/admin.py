from django.contrib import admin

# Register your models here.
from respy.models import Local,Equipamento,Aluguel,Funcionario


class LocalAdmin(admin.ModelAdmin):
    fields = ('nome',)
    list_display = ('local_id','nome')
    search_fields = ['name']

class EquipamentoAdmin(admin.ModelAdmin):
    fields = ('nome',)
    list_display = ('nome', 'equipamento_id')
    search_fields = ['name']

class FuncionarioAdmin(admin.ModelAdmin):
    fields = ('nome','email',)
    list_display = ('funcionario_id','nome', 'email')
    search_fields = ['name']

admin.site.register(Local,LocalAdmin)
admin.site.register(Equipamento, EquipamentoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)




