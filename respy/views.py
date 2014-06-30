from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
<<<<<<< HEAD
import model_report
=======
from respy.forms import AluguelForm
>>>>>>> c6837c3bd908e7fd08d83aa2e9b183b635bbc95b
from respy.models import *


def index(request):
    alugueisAtivos = Aluguel.objects.filter(ativo=True)
    alugueisFinalizados = Aluguel.objects.filter(ativo=False)[0:5]
    context = {
        'alugueis': alugueisAtivos,
        'alguelLen': alugueisAtivos.__len__(),
        'alugueisFinalizados': alugueisFinalizados,
    }
    return render_to_response('index.html', context, context_instance=RequestContext(request))
<<<<<<< HEAD
=======

@login_required
def novoAluguel(request):
    if request.method == 'POST':
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            response = {'Message': 'Aluguel inserido com sucesso', 'Success': True }
        else:
            response = {'Message': 'Erro ao inserir novo aluguel', 'Success': True }
    else:
        response = {'Message': 'Nada até aqui ocorreu', 'Success': False }

    form = AluguelForm()
    return render_to_response('novoAluguel.html', {'form': form, 'response': response}, RequestContext(request))


@login_required
def finalizarAluguel(request, id_aluguel):
    aluguel = Aluguel.objects.filter(aluguel_id=id_aluguel)
    aluguel.update(ativo=False)
    return redirect('/')

@login_required
def excluirAluguel(request, id_aluguel):
    aluguel = Aluguel.objects.filter(aluguel_id=id_aluguel)
    aluguel.delete()
    return redirect('/')
>>>>>>> c6837c3bd908e7fd08d83aa2e9b183b635bbc95b
