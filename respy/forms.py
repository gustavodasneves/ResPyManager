from django.db.models import Q
from django.forms import ModelForm
from respy.models import *


class AluguelForm(ModelForm):
    def is_valid(self):
        # run the parent validation first
        valid = super(AluguelForm, self).is_valid()

        # we're done now if not valid
        if not valid:
            return valid

        alugueis = Aluguel.objects.filter(Q(equipamento_id=self.cleaned_data['equipamento_id']))

        for aluguel in alugueis:
            if aluguel.ativo:
                return False

        return True

    class Meta:
        model = Aluguel
        fields = ['local_id', 'equipamento_id', 'funcionario_id', 'datahorainicio', 'datahorafim', 'ativo']

