from django.forms import ModelForm
from django import forms

from .models import Apontamento


class ApontamentoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ApontamentoForm, self).__init__(*args, **kwargs)
        self.fields['empresa'] = forms.CharField(required=False)
        self.fields['local'] = forms.CharField(required=False)

    class Meta:
        model = Apontamento
        fields = ['empresa', 'local']
