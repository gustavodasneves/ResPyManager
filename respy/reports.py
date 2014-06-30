from model_report.utils import count_column,yesno_format

__author__ = 'gustavoneves'
from respy.models import Aluguel
from model_report.report import reports, ReportAdmin

def date_format(value, instance):
    return value.strftime("%d/%m/%Y %H:%M")

class AluguelReport(ReportAdmin):
	global fields_orig,values
	model = Aluguel
	fields = [
		'local_id',
		'equipamento_id',
		'funcionario_id',
		'datahorainicio',
		'datahorafim',
		'ativo',
	]

	override_field_labels = {
    	'local_id': lambda x, y: ('Local'),
		'equipamento_id': lambda x, y: ('Equipamento'),
		'funcionario_id': lambda x, y: ('Funcionario'),
		'datahorainicio': lambda x, y: ('Inicio do aluguel'),
		'datahorafim': lambda x, y: ('Fim do aluguel'),
		'ativo': lambda x, y: ('Permanece alugado'),
	}
	override_field_formats = {
        'datahorafim': date_format,
		'datahorainicio': date_format,
		'ativo': yesno_format,
    }
	title = ('Relatorio de Alugueis')
	list_filter = ('funcionario_id','equipamento_id',)
	list_order_by = ('datahorainicio',)
	list_filter_queryset = {
        'local_id': {'groups__in': [1, 5]},
    }
	list_serie_fields = ('equipamento_id','ativo')
	type = 'report'

	chart_types = ('pie', 'column', 'line')


reports.register('aluguel-report', AluguelReport)
