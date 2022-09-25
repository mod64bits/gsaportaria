from django.db import models
from apps.base.models import BaseModelSlug
from apps.servicos.models import Servico


class Contato(BaseModelSlug):
    nome = models.CharField('Nome', max_length=60),
    whatsapp = models.CharField('Whatsapp')
    email = models.EmailField('E-mail')
    servico = models.CharField(Servico, max_length=30)
    mensagem = models.TextField('Mensagem')
    notificacao_whatsapp = models.BooleanField(
        'Deseja, Receber Informações de novidades dos nossos serviços por whatsapp', default=False)
    notificacao_email = models.BooleanField('Deseja, Receber Informações de novidades dos nossos serviços por email',
                                            default=False)
    slug_from = 'nome'

    def __str__(self):
        return f"Contato: {self.nome}"




