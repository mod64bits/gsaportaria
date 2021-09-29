from django.http import response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from apps.contatos.forms import ContatoForm
from django.views import View
from django.core import mail
from django.contrib import messages
from apps.servicos.models import Servico, Categoria, Imagem


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "servicos": Imagem.objects.all(),
            "servicos_categorias": Categoria.objects.all(),
            "form": ContatoForm(),
        }
        return render(request, 'home/Home.html', context)

    def post(self, request, *args, **kwargs):
        form = ContatoForm(request.POST)
        body = "Olá  sua mensagem foi recebida em breve retornaremos o contato."
        if form.is_valid():
            mail.send_mail(
                subject="Menssagem enviada com sucesso",
                message=body,
                from_email="contato@gsaportaria.com.br",
                recipient_list=["contato@gsaportaria.com.br"],
            )
            messages.success(request, 'e-mail enviado com sucesso!')
            return HttpResponseRedirect('/')




