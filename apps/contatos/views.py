from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core import mail
from django.contrib import messages
from .forms import ContatoForm


def remetente(email):
    mail.send_mail(
        subject="Menssagem recebida com sucesso",
        message="sua Mensagem foi recebida em breve entraremos em contato\n se preferir nos mande uma mensagem"
                "via whatsapp 19 99345-6524",
        from_email="contato@gsaportaria.com.br",
        recipient_list=[email],
    )


def destinatario(remetente, nome, telefone, mensagem):
    mail.send_mail(
        subject="Nova Mensagem via Site",
        message=f"Contato Nome: {nome}, \nemail: {remetente}, \ntelefone: {telefone}, \nenviou a seguinte mensagem: \n{mensagem}",
        from_email=remetente,
        recipient_list=["comercial2@gsaportaria.com.br", "gilsimar@gsaportaria.com.br"],
    )


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)

        if form.is_valid():
            remetente(form["email"].value())
            destinatario(
                form["email"].value(),
                form["nome"].value(),
                form["telefone"].value(),
                form["mensagem"].value(),
            )
            messages.success(request, 'e-mail enviado com sucesso!')
            return HttpResponseRedirect('/gsa/contato/')
        else:
            return render(request, 'contato/contato_form.html', {'form': form})
    else:
        context = {'form': ContatoForm()}
        return render(request, 'contato/contato_form.html', context)
