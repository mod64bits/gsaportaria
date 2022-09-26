from django.urls import path, re_path

from .views import ContatoFormView

app_name = 'contato'

urlpatterns = [
    path('', ContatoFormView.as_view(), name='contato'),
]
