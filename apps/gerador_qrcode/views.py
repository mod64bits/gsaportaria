from django.urls import reverse
from django.contrib import messages
from django.urls import reverse_lazy
from braces.views import PermissionRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from .models import QrCode
from .forms import NovoQrCodeForm


class NovoQrCodeView(PermissionRequiredMixin, CreateView):
    model = QrCode
    form_class = NovoQrCodeForm
    template_name = 'gerador_qrcode/novo_qrcode.html'
    permission_required = 'global_permissions.colaboradores'

    def get_success_url(self):
        messages.success(self.request, 'Qr Code Criado com Sucesso')
        return reverse('qrcode:lista_qr')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'active'
        return context


class ListaQrCodeView(PermissionRequiredMixin, ListView):
    model = QrCode
    paginate_by = 6
    context_object_name = 'qr_codes'
    template_name = 'gerador_qrcode/lista_qrcode.html'
    success_message = "%(local)s criado com sucesso"
    permission_required = 'global_permissions.colaboradores'

    def get_queryset(self):
        return QrCode.objects.all().order_by('-created_at')

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            local=self.object.local,
        )


class DetalheQrCodeView(DetailView):
    model = QrCode
    template_name = 'gerador_qrcode/detalhe.html'


class ImprimirQrCodeView(DetailView):
    model = QrCode
    template_name = 'gerador_qrcode/imprimir.html'


class DeleteQrCodeView(DeleteView):
    model = QrCode
    success_url = reverse_lazy('qrcode:lista_qr')

