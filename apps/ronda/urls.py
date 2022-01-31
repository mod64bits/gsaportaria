from django.urls import path, re_path
from .views import gerar_qrcode
from apps.core.views import Dashboard

app_name = 'ronda'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('novo/', gerar_qrcode, name='novo_qrs'),
]
