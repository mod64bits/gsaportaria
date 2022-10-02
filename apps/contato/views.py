from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from apps.core.envio_email import SendGSAMail
from .forms import ContatoForm
from .models import Contato


class ContatoFormView(SuccessMessageMixin, CreateView):
    model = Contato
    template_name = 'contato/contato_form.html'
    form_class = ContatoForm
    success_url = '/contato/'
    success_message = "%(nome)s , Mensagem enviada com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_contato'] = True
        return context

    def form_valid(self, form):
        subject = form.cleaned_data.get('departamento')
        nome = form.cleaned_data.get('nome')
        email = form.cleaned_data.get('email')
        whatsapp = form.cleaned_data.get('whatsapp')
        mensagem = form.cleaned_data.get('mensagem')

        email_mensagem = SendGSAMail(subject, nome, mensagem, whatsapp)
        email_mensagem.contato(servico=subject, email=email)

        return super().form_valid(form)
