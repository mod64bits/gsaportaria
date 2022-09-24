from .models import InformacoesDoSite
from apps.servicos.models import Categoria


def site_infor(request):
    return {
        "site_infor": InformacoesDoSite.objects.first()
    }


def servicos_categorias(request):
    return {
        "categorias_servicos": Categoria.objects.all()
    }

