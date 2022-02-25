from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import QrCode
from .forms import NovoQrCodeForm


class NovoQrCodeView(LoginRequiredMixin, CreateView):
    model = QrCode
    form_class = NovoQrCodeForm
    template_name = 'gerador_qrcode/novo_qrcode.html'

    def get_success_url(self):
        return reverse('qrcode:lista_qr')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'active'
        return context


class ListaQrCodeView(LoginRequiredMixin, ListView):
    model = QrCode
    paginate_by = 6
    context_object_name = 'qr_codes'
    template_name = 'gerador_qrcode/lista_qrcode.html'

    def get_queryset(self):
        return QrCode.objects.all().order_by('-created_at')
