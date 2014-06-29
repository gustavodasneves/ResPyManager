from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from respy.forms import AluguelForm
from respy.models import *

def index(request):
    alugueisAtivos = Aluguel.objects.filter(ativo = True)
    context = {'alugueis' : alugueisAtivos, 'alguelLen' : alugueisAtivos.__len__()}
    return render_to_response('index.html', context, context_instance=RequestContext(request))

@login_required
def novoAluguel(request):
    if request.method == 'POST':
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()

            response = {'Message': 'Inserido com sucesso', 'Success': True }
    else:
        response = {'Message': 'Nada até aqui ocorreu', 'Success': False }

    form = AluguelForm()
    return render_to_response('novoAluguel.html', {'form': form, 'response': response}, RequestContext(request))


