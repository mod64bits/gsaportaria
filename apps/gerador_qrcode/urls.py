from django.urls import path, re_path
from .views import(NovoQrCodeView, ListaQrCodeView, DetalheQrCodeView,
                   ImprimirQrCodeView, DeleteQrCodeView)

app_name = 'qrcode'

urlpatterns = [
    path('novo/', NovoQrCodeView.as_view(), name='novo_qr'),
    path('lista/', ListaQrCodeView.as_view(), name='lista_qr'),
    path('qrcode/<int:pk>/', DetalheQrCodeView.as_view(), name='detalhe_qr'),
    path('imprimir/<int:pk>/', ImprimirQrCodeView.as_view(), name='imprimir_qr'),
    path('delete/<int:pk>/', DeleteQrCodeView.as_view(), name='delete_qr'),
]
