from io import BytesIO

import qrcode
from PIL import Image, ImageDraw
from django.core.files import File
from django.forms import ModelForm
from .models import QrCode
from apps.empresas.models import Empresa


class NovoQrCodeForm(ModelForm):
    class Meta:
        model = QrCode
        fields = '__all__'

    def save(self, commit=True, *args, **kwargs):
        instance = super(NovoQrCodeForm, self).save(commit=False)
        empresa = Empresa.objects.get(id=int(self.data['empresa']))
        qr_codeimg = qrcode.make(
            f"{empresa.nome},{self.data['local']}")
        canvas = Image.new('RGB', (300, 300), 'white')
        draw = ImageDraw.Draw(canvas)

        canvas.paste(qr_codeimg)
        fname = f"qr_code-{empresa.nome}_{self.data['local']}.png"

        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        instance.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


