from rest_framework import routers, serializers
from apps.apontamento.models import Apontamento


class ApontamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apontamento
        fields = ['empresa', 'local']
