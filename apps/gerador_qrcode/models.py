from django.db import models
from django.urls import reverse

from apps.empresas.models import Empresa


class QrCode(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT,
                                related_name='empresa_qr',
                                verbose_name='Empresa')
    local = models.CharField('Local', max_length=100)
    qr_code = models.ImageField("QR Code", upload_to='qr-codes', blank=True)
    created_at = models.DateTimeField('Cadastrado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)

    def get_absolute_url(self):
        return reverse('ronda:dashboard')

    def __str__(self):
        return self.local


