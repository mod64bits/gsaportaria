from django.views.generic.edit import FormView
from .forms import ContatoForm


class ContatoFormView(FormView):
    template_name = 'contato/contato_form.html'
    form_class = ContatoForm
    success_url = '/contato/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
