from django.urls import path
from .views import RegistroNovoView, RegistroListaView, ListaRegistrosView

app_name = 'apontamento'

urlpatterns = [
    path('', ListaRegistrosView.as_view(), name='list_registro'),
    path('registros/', RegistroListaView.as_view(), name='usuario_registro'),
    path('novo/', RegistroNovoView.as_view(), name='novo_registro'),
]
