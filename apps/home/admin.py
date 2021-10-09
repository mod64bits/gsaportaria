from django.contrib import admin
from .models import Parceiros


class ParceirosAdmin(admin.ModelAdmin):
    list_filter = ['ativo', 'nome', 'created_at']
    search_fields = ('titulo',)


admin.site.register(Parceiros, ParceirosAdmin)
