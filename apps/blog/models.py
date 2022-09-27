from django.db import models
from apps.base.models import BaseModelSlug, BaseModelUUID
from apps.servicos.models import Servico
from django.contrib.contenttypes.fields import GenericRelation
from apps.tag.models import Tag
from django.utils.text import slugify
import string
from random import SystemRandom


class PostesCategoria(BaseModelUUID):
    nome = models.CharField("Poste Categoria", max_length=100)

    def __str__(self):
        return self.nome


class Postes(BaseModelSlug):
    titulo = models.CharField('Titulo', max_length=50)
    categoria = models.ForeignKey(
        PostesCategoria,
        verbose_name="Categoria",
        related_name="post_categoria",
        on_delete=models.CASCADE
    )
    servico = models.ForeignKey(
        Servico,
        verbose_name="Serviço",
        related_name="post_servico",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    conteudo = models.TextField('Conteúdo')
    slug = models.SlugField('Slug', unique=True)
    tags = GenericRelation(Tag, related_query_name='posts-tags')

    def save(self, *args, **kwargs):
        if not self.slug:
            rand_letters = ''.join(
                SystemRandom().choices(
                    (string.ascii_letters + string.digits),
                    k=4,
                )
            )
            self.slug = slugify(f'{self.titulo}-{rand_letters}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
