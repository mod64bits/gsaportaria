from django.db import models
from apps.base.models import BaseModelUUID
from apps.servicos.models import Servico
from apps.core.envio_email import SendGSAMail


class SolicitacaoDeOrcamentoManege(models.Manager):
    def nova_solicitacai_orcamento(self, servico, data):
        self.create(
            servico=servico,
            nome=data['nome'],
            email=data['email'],
            whatsapp=data['whatsapp'],
            mensagem=data['mensagem']
        )

        enviar_email_solicitacao = SendGSAMail(
            "Solicitação De Orçamento",
            nome=data['nome'],
            whatsapp=data['whatsapp'],
            mensagem=data['mensagem'],

        )
        enviar_email_solicitacao.solicitacao_orcamento(servico=servico, to=[data['email']])
        contato = SendGSAMail(
            "Solicitação De Orçamento",
            nome=data['nome'],
            whatsapp=data['whatsapp'],
            mensagem=data['mensagem'],
        )
        contato.solicitacao_orcamento_gsa(servico=servico, to=[data['email']])


class SolicitacaoDeOrcamento(BaseModelUUID):
    objects = SolicitacaoDeOrcamentoManege()
    servico = models.ForeignKey(
        Servico,
        on_delete=models.CASCADE,
        verbose_name="Servico",
        related_query_name="servico_solicitacao",
        related_name="servico_orcamento"
    )
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('Email')
    whatsapp = models.CharField("WhatsApp", max_length=30)
    mensagem = models.TextField('Mensagem', null=True, blank=True)

    def __str__(self):
        return self.nome
