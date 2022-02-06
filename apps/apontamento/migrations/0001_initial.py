# Generated by Django 2.2 on 2022-02-06 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apontamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=100, verbose_name='Local')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresa_apontamento', to='empresas.Empresa')),
            ],
        ),
    ]
