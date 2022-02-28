from django.conf import settings
from django.db import models

from apps.empresas.models import Empresa


class ApontamentoBase(models.Model):


    local = models.CharField('Local', max_length=100)
    created_at = models.DateTimeField('Cadastrado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.local

    class Meta:
        abstract = True


class Apontamento(ApontamentoBase):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.PROTECT,
                                related_name='user_apontamento')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,
                                related_name='empresa_apontamento')


class ApontamentoLimpeza(ApontamentoBase):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.PROTECT,
                                related_name='user_apont_limpeza')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,
                                related_name='empre_apont_limp')

