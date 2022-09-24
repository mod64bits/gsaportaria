from django.db import models
from apps.base.models import BaseModelUUID


class Parceiros(BaseModelUUID):
    ativo = models.BooleanField('Ativo?', default=True)
    nome = models.CharField('Nome', max_length=100)
    logo = models.ImageField('Logo', upload_to='parceiros', default='media/parceiro.jpg')

    class Meta:
        ordering = ["created_at"]
        verbose_name_plural = "Parceiros"

    def __str__(self):
        return self.nome


class Solucoes(BaseModelUUID):
    nome = models.CharField('Solução', max_length=50)
    icone = models.ImageField(upload_to='solucoes/imagens')
    descricao = models.TextField('Soluções')

    def __str__(self):
        return self.nome


class InformacoesDoSite(BaseModelUUID):
    nome = models.CharField('Nome do Site', max_length=25)
    telefone = models.CharField('Telefone', max_length=30)
    email = models.EmailField('e-mail')
    endereco = models.CharField('Endereço', max_length=200)
    facebook = models.URLField('Facebook', null=True, blank=True)
    instagram = models.URLField('Facebook', null=True, blank=True)
    sobre = models.TextField('Sobre', null=True, blank=True)
    escolha = models.TextField('Porque escolher-nos', null=True, blank=True)

    def __str__(self):
        return self.nome
