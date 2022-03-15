from datetime import datetime
from datetime import timedelta
from datetime import date
from django.urls import reverse_lazy
from dateutil.parser import parse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from apps.users.models import User
from .models import Apontamento, Empresa, ApontamentoLimpeza

from .forms import ApontamentoForm

from braces.views import PermissionRequiredMixin
from django.views import View
from django.views.generic import ListView


class RegistroListaView(LoginRequiredMixin, ListView):
    model = Apontamento
    paginate_by = 10
    context_object_name = 'registros'
    template_name = 'apontamento/apontamento.html'
    success_url = reverse_lazy('list_notes')

    # login_url = '/login/'
    # redirect_field_name = '/apontamento/registros/'

    def get_queryset(self):
        return Apontamento.objects.filter(usuario_id=self.request.user.id)


class RegistroNovoView(LoginRequiredMixin, View):
    form_class = ApontamentoForm
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'apontamento/novo_registro.html'

    def get_success_url(self):
        messages.success(self.request, 'Qr Code Criado com Sucesso')
        return reverse('qrcode:lista_qr')

    def get(self, request):
        context = {
            'form': self.form_class
        }
        return render(request, self.template_name, context)

    def post(self, request):
        empresa = Empresa.objects.get(nome=request.POST.get('empresa'))
        local = request.POST.get('local')

        Apontamento.objects.create(
            usuario=User.objects.get(id=self.request.user.id),
            empresa=empresa,
            local=local
        )

        return redirect('apontamento:list_registro')


class ListaRegistrosView(PermissionRequiredMixin, ListView):
    model = Apontamento
    paginate_by = 15
    template_name = 'apontamento/todos_apontamentos.html'
    context_object_name = 'registros'
    permission_required = 'global_permissions.colaboradores'

    def buscas(self, usuario=None, data=None, datafim=None, dias=None):
        # objects.filter(creation_date__gte=datetime.today() - timedelta(days=30))
        # filtro por dia
        user = ''

        if dias:
            dia = int(dias)

        if data:
            data = parse(data)
        if datafim:
            datafim = parse(datafim)
        if usuario:
            user = User.objects.get(username=usuario)

        if usuario is None and data is None and dias is None:
            """Retorna todos os usuarios Get Inicial"""
            return Apontamento.objects.all().order_by('-updated_at')

        if dias is not None and data is None and usuario is not None:
            """Retorna apontamentos pela quantidade de dias informados"""
            busca = Apontamento.objects.filter(usuario=int(user.id)).filter(
                created_at=date.today() - timedelta(int(dias))
            )
            return busca

        if dias is not None and usuario is None and data is None:
            """Retorna Apontamento do nos dias informados"""
            busca = Apontamento.objects.filter(
                created_at=date.today() - timedelta(int(dias))
            )
            return busca

        if usuario is not None and data is None:
            """Retorna todos os apontamentos do usuario"""
            busca = Apontamento.objects.filter(usuario=int(user.id))
            return busca

        if usuario is not None and data is not None and datafim is None:
            """Retorna apontamentos com filtro de apontamenos 
            por usuario e data"""
            busca = Apontamento.objects.filter(usuario=int(user.id)).filter(
                created_at__gte=data)
            return busca

        if data is not None and datafim is None and usuario is None:
            """Retorna todo apontamento de uma determinada data"""
            busca = Apontamento.objects.filter(created_at__gte=data)
            return busca

        if usuario and data and datafim:
            """Retorna os apontamentos de um range de data por usuario"""
            busca = Apontamento.objects.filter(usuario=int(user.id)).filter(
                created_at__range=[data, datafim]
            )
            return busca
        if data is not None and datafim is not None and usuario is None:
            """Retorna todos os apontamentos em um range de data"""
            busca = Apontamento.objects.filter(created_at__range=[data, datafim])
            return busca

    def prepare_busca(self, data):
        """Ficou feio pra caralho essa porra mas ta funcionado"""
        usuario = ""
        _data = ""
        _datafim = ""
        dia_busca = ""
        if data.get('select_usuarios') == "Selecione o Usuário" or data.get('select_usuarios') == '':
            usuario = None
        else:
            usuario = data.get('select_usuarios')

        if data.get('dias') == "Selecione range de dias" or data.get('dias') == '':
            dia_busca = None
        else:
            dia_busca = data.get('dias', None)
        if data.get('data') == '':
            _data = None
        else:
            _data = data.get('data')
        if data.get('data_fim') == '':
            _datafim = None
        else:
            _datafim = data.get('data_fim')

        busca_resultado = self.buscas(
            usuario=usuario,
            data=_data,
            datafim=_datafim,
            dias=dia_busca
        )
        # Organizar as regras da busca

        return busca_resultado

    def get_queryset(self):
        busca_resultado = self.prepare_busca(self.request.GET)
        return busca_resultado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuarios'] = User.objects.all().order_by('-username')
        return context


class MeusApontamentosLimpesa(ListView):
    model = ApontamentoLimpeza
    paginate_by = 10
    context_object_name = 'registros_limpeza'
    template_name = 'apontamento/apontamento.html'
    success_url = reverse_lazy('list_notes')
    login_url = '/login/'
    redirect_field_name = '/questonario/'

    def get_queryset(self):
        return ApontamentoLimpeza.objects.filter(
            usuario_id=self.request.user.id)
