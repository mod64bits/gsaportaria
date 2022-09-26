from django.db import models
from apps.base.models import BaseModelSlug, BaseModelUUID
from apps.servicos.models import Servico
from apps.core.signals import create_slug
from django.db.models import signals


class Departamento(BaseModelUUID):
    nome = models.CharField('Departamento', max_length=30)
    ativo = models.BooleanField('Ativo?', default=True)

    def __str__(self):
        return self.nome


class Contato(BaseModelSlug):
    nome = models.CharField('Nome', max_length=60)
    whatsapp = models.CharField('Whatsapp', max_length=20)
    email = models.EmailField('E-mail')
    departamento = models.CharField("Departamento", max_length=30)
    mensagem = models.TextField('Mensagem')
    notificacao_whatsapp = models.BooleanField(
        'Deseja, Receber Informações de novidades dos nossos serviços por whatsapp', default=False)
    notificacao_email = models.BooleanField('Deseja, Receber Informações de novidades dos nossos serviços por email',
                                            default=False)
    slug_from = 'nome'

    def __str__(self):
        return f"Contato: {self.nome}"


signals.post_save.connect(create_slug, sender=Contato)