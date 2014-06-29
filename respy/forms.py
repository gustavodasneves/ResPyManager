from django.forms import ModelForm
from respy.models import *


class AluguelForm(ModelForm):
    class Meta:
        model = Aluguel
        fields = ['local_id', 'equipamento_id', 'funcionario_id', 'datahorainicio', 'datahorafim', 'ativo']

