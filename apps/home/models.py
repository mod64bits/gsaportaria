from django.db import models
import uuid


class Parceiros(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ativo = models.BooleanField('Ativo?', default=True)
    nome = models.CharField('Nome', max_length=100)
    seguimento = models.CharField('Seguimento', max_length=100)
    resumo = models.TextField('Resumo')
    logo = models.ImageField('Logo', upload_to='parceiros', default='media/parceiro.jpg')
    site = models.CharField('Site', max_length=150, null=True, blank=True, default='#')
    facebook = models.CharField('Facebook', max_length=150, null=True, blank=True, default='#')
    instagram = models.CharField('Instagram', max_length=150, null=True, blank=True, default='#')
    created_at = models.DateTimeField('Cadastrado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Parceiros"

    def __str__(self):
        return f"Nome: {self.nome} Seguimento: {self.seguimento}"

