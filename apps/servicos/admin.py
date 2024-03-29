try:
    import Image
except ImportError:
    from PIL import Image

from django import forms

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from django.contrib.admin.options import ModelAdmin
from apps.tag.models import Tag
from apps.servicos.models import Servico, Categoria, Imagem


class TagInline(GenericStackedInline):
    model = Tag
    fields = 'name',
    extra = 0


class ImageInline(admin.StackedInline):
    model = Imagem
    extra = 1


class AdminCategoria(ModelAdmin):
    list_display = ('titulo', 'created_at',)
    list_filter = ('titulo',)
    search_fields = ('titulo',)


class ServicoAdmin(ModelAdmin):
    list_display = ('id', 'titulo', 'slug', 'created_at',)
    list_display_links = ('id', 'slug',)
    list_editable = ('titulo',)
    list_filter = ('titulo',)
    search_fields = ('titulo',)
    inlines = [
        TagInline,
    ]


class AdminImagem(ModelAdmin):
    list_display = ('titulo',)
    list_filter = ('titulo',)
    search_fields = ('titulo',)


admin.site.register(Servico, ServicoAdmin)
admin.site.register(Imagem)
admin.site.register(Categoria)
