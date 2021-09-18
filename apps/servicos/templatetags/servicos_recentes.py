from django import template
from apps.servicos.models import Imagem, Servico

register = template.Library()

@register.simple_tag(takes_context=True)
def lista_servicos(context):
    servicos = Imagem.objects.filter(servico__slug=context)
    return servicos
