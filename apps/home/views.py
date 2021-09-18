from django.http import response
from django.shortcuts import render
from django.views.generic import TemplateView
from functools import reduce
from queryset_sequence import QuerySetSequence
from django.views import View
from apps.servicos.models import Servico, Categoria, Imagem


class HomeView(View):


    def get(self, request, *args, **kwargs):
        context = {
            "servicos": Imagem.objects.all(),
            "servicos_categorias": Categoria.objects.all(),
        }

        return render(request, 'home/Home.html', context)
