from django.views.generic.base import TemplateView
from apps.servicos.models import Servico, ServicosDestaques, Categoria
from .models import Parceiros


class HomeView(TemplateView):
    template_name = 'home/Home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousels_home'] = self.get_carousel()
        context['destaques'] = self.get_destaques()
        context['servicos_home'] = self.get_servicos_home()
        context['parceiros'] = Parceiros.objects.filter(ativo=True)
        context['active_home'] = True
        return context

    def get_carousel(self):
        return Servico.objects.filter(slider=True)

    def get_destaques(self):
        destaques = ServicosDestaques.objects.all()
        cont = 1
        dados = []

        for item in destaques:
            dados.append(
                {
                    "nome": item.nome,
                    "icone": item.icone,
                    "descricao": item.descricao,
                    "style_time": f"0.{cont}s",
                    "numero": cont
                }
            )
            cont += 1

        return dados

    def get_servicos_home(self):
        servicos_home = Servico.objects.filter(ativo=True)[:9]
        cont = 1
        dados = []

        for item in servicos_home:
            dados.append({
                "id": item.id,
                "nome": item.titulo,
                "imagem": item.imagem,
                "categoria": item.categoria,
                "descricao": item.descricao,
                "slug": item.slug,
                "time": f"0.{cont}s"
            })
            cont += 1

        return dados
