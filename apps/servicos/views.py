from django.urls import reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from apps.servicos.models import Servico
from django.views.generic.list import ListView
from apps.orcamentos.models import SolicitacaoDeOrcamento
from .filters import Servicosfilters
from django.contrib import messages


class ServicoDetalhe(SuccessMessageMixin, DetailView):
    model = Servico
    template_name = 'servicos/ServicoDetalhe.html'
    success_message = "%(nome)s , Mensagem enviada com sucesso!"

    def post(self, request, **kwargs):
        servico = Servico.objects.get(slug=kwargs['slug'])
        data = request.POST
        SolicitacaoDeOrcamento.objects.nova_solicitacai_orcamento(servico, data)
        messages.add_message(
            request, messages.SUCCESS, f"{data.get('nome', '')}, Sua Mensagem foi Enviada com Sucesso"
        )

        return redirect(servico)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['tags'] = True
        return context


class ServicoBaseView(View):
    model = Servico
    success_url = reverse_lazy('servicos:servicos')
    context_object_name = 'servico_all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        filter = Servicosfilters(self.request.GET, queryset)
        context["filter"] = filter
        return context


class ServicosView(ServicoBaseView, ListView):
    model = Servico
    context_object_name = 'servicos'
    template_name = 'servicos/Servicos.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Servico.objects.all()
        filter = Servicosfilters(self.request.GET, queryset)
        return filter.qs
