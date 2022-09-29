from django.urls import path, re_path
from .views import ServicoDetalhe, ServicosView

app_name = 'servicos'

urlpatterns = [
    path('servicos/', ServicosView.as_view(), name='servicos'),
    path('<slug:slug>/', ServicoDetalhe.as_view(), name='servico_detalhe'),
]
