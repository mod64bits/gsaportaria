import os
from django.utils.html import strip_tags
from email.mime.image import MIMEImage
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class SendGSAMail:
    def __init__(self, subject, nome, mensagem, whatsapp):
        self.subject = subject
        self.nome = nome
        self.whatsapp = whatsapp
        self.mensagem = mensagem

    def solicitacao_orcamento(self, servico, to=[]):
        context = {
            "nome": self.nome,
            "email": to,
            "servico": servico,
            "whatsapp": self.whatsapp,
            "mensagem": self.mensagem
        }
        html_content = render_to_string('emails/solicitacao_orcamento.html', context)
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(
            self.subject,
            text_content,
            "contato@gsaportaria.com.br",
            to
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    def solicitacao_orcamento_gsa(self, servico, to=[]):
        context = {
            "nome": self.nome,
            "email": to,
            "servico": servico,
            "whatsapp": self.whatsapp,
            "mensagem": self.mensagem
        }
        html_content = render_to_string('emails/solicitacao_orcamento_gsa.html', context)
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(
            self.subject,
            text_content,
            "contato@gsaportaria.com.br",
            to
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    def contato(self, servico, email):
        context = {
            "nome": self.nome,
            "email": email,
            "servico": servico,
            "whatsapp": self.whatsapp,
            "mensagem": self.mensagem
        }
        html_content = render_to_string('emails/solicitacao_orcamento_gsa.html', context)
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(
            self.subject,
            text_content,
            "contato@gsaportaria.com.br",
            ["gilsimar@gsaportaria.com.br"]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()


    # TODO: Melhorar classe de envio de email
