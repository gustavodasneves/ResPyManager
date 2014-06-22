from django.core import serializers
from django.shortcuts import render
from respy.models import Equipamento
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the index view")

def equipamentos(request):
    lista_equipamentos = Equipamento.objects.all()
    data = serializers.serialize("json", lista_equipamentos)
    return HttpResponse(data, content_type = "application/json")

def inserir_equipamento(request):
    request._body
