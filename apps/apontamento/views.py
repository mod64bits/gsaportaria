from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from braces.views import PermissionRequiredMixin
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Apontamento, Empresa, ApontamentoLimpeza
from .forms import ApontamentoForm
from apps.users.models import User


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



    def get_queryset(self):
        return Apontamento.objects.all().order_by('-created_at')


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
