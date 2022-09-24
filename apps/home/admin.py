from django.contrib import admin
from .models import Parceiros, InformacoesDoSite
from apps.servicos.models import ServicosDestaques



class ParceirosAdmin(admin.ModelAdmin):
    list_filter = ['ativo', 'nome', 'created_at']
    search_fields = ('titulo',)


class InformacoesSiteAdmin(admin.ModelAdmin):
    list_filter = ['nome', 'created_at']
    search_fields = ('nome',)


class ServicosDestaquesAdmin(admin.ModelAdmin):
    list_filter = ['nome', 'created_at']
    search_fields = ('nome',)


admin.site.register(InformacoesDoSite, InformacoesSiteAdmin)
admin.site.register(Parceiros, ParceirosAdmin)
admin.site.register(ServicosDestaques, ServicosDestaquesAdmin)
