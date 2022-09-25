from django import forms
from .models import Contato
from apps.servicos.models import Servico


class ContatoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContatoForm, self).__init__(*args, **kwargs)

        self.fields['servico'] = forms.CharField(label="Serviços", max_length=30,
                                                 widget=forms.Select(choices=self.get_servicos()))

    def get_servicos(self):
        items = Servico.objects.filter(ativo=True).values('titulo')
        choice = []
        for item in items:
            choice.append(
                (item['titulo'].replace(' ', '').capitalize(), item['titulo'].title()))
        return choice

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

    class Meta:
        model = Contato
        fields = '__all__'
