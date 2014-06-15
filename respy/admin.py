from django.contrib import admin

# Register your models here.
from respy.models import Local,Equipamento,Aluguel


class LocalAdmin(admin.ModelAdmin):
    fields = ('local_id','nome')
    list_display = ('local_id','nome')

class EquipamentoAdmin(admin.ModelAdmin):
    fields = ('equipamento_id','nome')
    list_display = ('equipamento_id','nome')

class AluguelAdmin(admin.ModelAdmin):
    fields = ('aluguel_id','local_id','equipamento_id','user_id','datahorainicio','datahorafim','ativo')
    list_display = ('aluguel_id','local_id','equipamento_id','user_id','datahorainicio','datahorafim','ativo')


admin.site.register(Local,LocalAdmin )
admin.site.register(Equipamento, EquipamentoAdmin)
admin.site.register(Aluguel,AluguelAdmin)




