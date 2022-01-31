from django.urls import path
from .views import RegistroNovoView, RegistroListaView

app_name = 'apontamento'

urlpatterns = [
    path('', RegistroListaView.as_view(), name='list_registro'),
    path('novo/', RegistroNovoView.as_view(), name='novo_registro'),
]
