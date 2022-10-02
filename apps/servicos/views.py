from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from apps.servicos.models import Servico, Imagem
from django.views.generic.list import ListView
from apps.orcamentos.models import SolicitacaoDeOrcamento

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


class ServicosView(ListView):
    model = Servico
    context_object_name = 'servicos'
    template_name = 'servicos/Servicos.html'
