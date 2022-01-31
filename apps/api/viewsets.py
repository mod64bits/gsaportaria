from rest_framework import viewsets
from apps.apontamento.models import Apontamento
from .serializers import ApontamentoSerializer


class ApontamentoViewSet(viewsets.ModelViewSet):
    queryset = Apontamento.objects.all()
    serializer_class = ApontamentoSerializer