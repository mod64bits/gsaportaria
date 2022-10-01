from django.views.generic.detail import DetailView
from apps.servicos.models import Servico, Imagem
from django.views.generic.list import ListView
from apps.orcamentos.models import SolicitacaoDeOrcamento
from apps.core.envio_email import SendGSAMail

from django.http import HttpResponseRedirect


class ServicoDetalhe(DetailView):
    model = Servico
    template_name = 'servicos/ServicoDetalhe.html'

    def post(self, request, **kwargs):
        servico = Servico.objects.get(slug=kwargs['slug'])
        data = request.POST
        SolicitacaoDeOrcamento.objects.nova_solicitacai_orcamento(servico, data)

        return HttpResponseRedirect("/")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['tags'] = True
        return context


class ServicosView(ListView):
    model = Servico
    context_object_name = 'servicos'
    template_name = 'servicos/Servicos.html'
