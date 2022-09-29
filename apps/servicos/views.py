from django.views.generic.detail import DetailView
from apps.servicos.models import Servico, Imagem
from django.views.generic.list import ListView


class ServicoDetalhe(DetailView):
    model = Servico
    template_name = 'servicos/ServicoDetalhe.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['imagens'] = Imagem.objects.filter(servico_id=self.imagens_servicos)
        return context


class ServicosView(ListView):
    model = Servico
    context_object_name = 'servicos'
    template_name = 'servicos/Servicos.html'