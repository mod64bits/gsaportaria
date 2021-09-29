from django.urls import path, re_path
from .views import HomeView
from apps.contatos.views import contato

app_name = 'home'

urlpatterns = [
    path('contato/', contato, name='contato'),
    path('', HomeView.as_view(), name='home'),
]
