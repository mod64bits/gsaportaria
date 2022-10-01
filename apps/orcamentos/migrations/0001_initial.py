# Generated by Django 4.0.7 on 2022-09-29 23:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitacaoDeOrcamento',
            fields=[
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Cadastrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado em')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('whatsapp', models.CharField(max_length=30, verbose_name='WhatsApp')),
                ('mensagem', models.TextField(blank=True, null=True, verbose_name='Mensagem')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servico_orcamento', related_query_name='servico_solicitacao', to='servicos.servico', verbose_name='Servico')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
