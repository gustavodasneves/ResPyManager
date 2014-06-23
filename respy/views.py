from django.shortcuts import render_to_response
from django.template import RequestContext
from respy.models import *
from django.http import HttpResponse

def index(request):
    alugueisAtivos = Aluguel.objects.filter(ativo = True)
    context = {'alugueis' : alugueisAtivos, 'alguelLen' : alugueisAtivos.__len__()}
    return render_to_response('index.html', context, context_instance=RequestContext(request))

