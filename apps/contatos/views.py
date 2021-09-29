from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core import mail
from django.contrib import messages
from .forms import ContatoForm


def contato(request):
    if request.method == 'POST':
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
            return HttpResponseRedirect('/gsa/contato/')
        else:
            return render(request, 'contato/contato_form.html', {'form': form})
    else:
        context = {'form': ContatoForm()}
        return render(request, 'contato/contato_form.html', context)
