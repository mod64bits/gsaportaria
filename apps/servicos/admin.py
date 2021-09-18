try:
    import Image
except ImportError:
    from PIL import Image

from django import forms

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from apps.servicos.models import Servico, Categoria, Imagem


class ImageInline(admin.StackedInline):
    model = Imagem
    extra = 1


class AdminCategoria(ModelAdmin):
    list_display = ('titulo', 'created_at',)
    list_filter = ('titulo',)
    search_fields = ('titulo',)


class AdminServico(ModelAdmin):
    list_display = ('titulo', 'created_at',)
    list_filter = ('titulo',)
    search_fields = ('titulo',)
    inlines = [ImageInline]


class AdminImagem(ModelAdmin):
    list_display = ('titulo', )
    list_filter = ('titulo', )
    search_fields = ('titulo', )






admin.site.register(Servico, AdminServico)
admin.site.register(Imagem)
admin.site.register(Categoria)
