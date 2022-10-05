import django_filters
from .models import Servico


class Servicosfilters(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Servico
        fields = ['titulo']
