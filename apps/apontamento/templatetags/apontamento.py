from django import template
from django.template.defaultfilters import stringfilter
from apps.apontamento.models import Apontamento

register = template.Library()


def verificar_tempo(data, id_data):
    
    data_inicial = Apontamento.objects.filter(id=id_data).values('created_at')
    data_final = Apontamento.objects.filter(id=id_data + 1).values('created_at')





