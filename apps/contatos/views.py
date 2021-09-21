from django.shortcuts import render
from .forms import ContatoForm


def contato(request):
    context = {'form': ContatoForm()}
    return render(request, 'contato/contato_form.html', context)
