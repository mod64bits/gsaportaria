from django.urls import path, re_path
from .views import NovoQrCodeView, ListaQrCodeView

app_name = 'qrcode'

urlpatterns = [
    path('novo/', NovoQrCodeView.as_view(), name='novo_qr'),
    path('lista/', ListaQrCodeView.as_view(), name='lista_qr'),
]
