# Generated by Django 3.2 on 2022-01-14 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NovoQrCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=100, verbose_name='Local')),
                ('qr_code', models.ImageField(blank=True, upload_to='qr-codes', verbose_name='QR Code')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='empresa_qr', to='empresas.empresa', verbose_name='Empresa')),
            ],
        ),
    ]
