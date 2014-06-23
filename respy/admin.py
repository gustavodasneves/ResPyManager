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

class AluguelAdmin(admin.ModelAdmin):
    fields = ('local_id','equipamento_id','funcionario_id','datahorainicio','datahorafim','ativo',)
    list_display = ('aluguel_id','local_id','equipamento_id','funcionario_id','datahorainicio','datahorafim','ativo')

class FuncionarioAdmin(admin.ModelAdmin):
    fields = ('nome',)
    list_display = ('funcionario_id','nome')
    search_fields = ['name']

admin.site.register(Local,LocalAdmin)
admin.site.register(Equipamento, EquipamentoAdmin)
admin.site.register(Aluguel,AluguelAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)




