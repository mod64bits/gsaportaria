from django import forms
from .models import Contato, Departamento


class ContatoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContatoForm, self).__init__(*args, **kwargs)


        self.fields['departamento'] = forms.CharField(label="Departamento", max_length=30,
                                                      widget=forms.Select(choices=self.get_servicos()))

    def get_servicos(self):
        items = Departamento.objects.filter(ativo=True).values('nome')
        choice = []
        for item in items:
            choice.append(
                (item['nome'].replace(' ', '').capitalize(), item['nome'].title()))
        return choice

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

    class Meta:
        model = Contato
        fields = '__all__'
