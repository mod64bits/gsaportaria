from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
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
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
