from django.db import models
import uuid
from django.urls import reverse
from apps.base.models import BaseModelSlug, BaseModelUUID
from apps.core.signals import create_slug
from django.db.models import signals


class Categoria(BaseModelSlug):
    nome = models.CharField('Categoria', max_length=30)
    slug_from = 'nome'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('catalog:category', kwargs={'slug': self.slug})

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Categorias"


class Servico(BaseModelSlug):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField('Servico', max_length=150)
    imagem = models.ImageField(upload_to='servicos/imagens', default='media/servico_padrao.jpg')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='cat_servicos')
    ativo = models.BooleanField('Ativo', default=True)
    slider = models.BooleanField('Slider', default=False)
    descricao = models.TextField('Descrição')

    slug_from = 'titulo'

    def __str__(self):
        return self.titulo.title()

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Serviços"


class Imagem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField('Imagem nome', max_length=15)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='img_servico')
    ativo = models.BooleanField('Ativo', default=True)
    slider = models.BooleanField('Ativo', default=False)
    imagem = models.ImageField(null=True, blank=True, upload_to='galeria/original')
    created_at = models.DateTimeField('Cadastrado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Imagens"


class ServicosDestaques(BaseModelUUID):
    nome = models.CharField('Servico', max_length=50)
    icone = models.ImageField(upload_to='servicos/imagens')
    descricao = models.TextField('Descrição')

    def __str__(self):
        return self.nome


signals.post_save.connect(create_slug, sender=Categoria)
signals.post_save.connect(create_slug, sender=Servico)
