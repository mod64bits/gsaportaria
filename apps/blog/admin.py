from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import Postes, PostesCategoria
from apps.tag.models import Tag


class TagInline(GenericStackedInline):
    model = Tag
    fields = 'name',
    extra = 1

@admin.register(Postes)
class PostesAdmin(admin.ModelAdmin):
    list_display = 'id', 'titulo', 'slug',
    list_display_links = 'id', 'slug',
    search_fields = 'id', 'slug', 'titulo',
    list_per_page = 20
    list_editable = 'titulo',
    ordering = '-id',
    prepopulated_fields = {
        'slug': ('titulo',),
    }

    inlines = [
        TagInline,
    ]


@admin.register(PostesCategoria)
class PostesCategoriaAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome',
    list_display_links = 'nome',
    search_fields = 'id', 'nome',
    list_per_page = 20
    ordering = '-id',
