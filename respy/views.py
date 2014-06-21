from django.core import serializers
from django.shortcuts import render
from respy.models import Equipamento
from django.http import HttpResponse

# Create your views here.


def equipamentos(request):
    data = {}
    lista_equipamentos = Equipamento.objects.all()
    data = serializers.serialize("json", lista_equipamentos)
    return HttpResponse(data, content_type = "application/json")
