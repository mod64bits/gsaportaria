# Generated by Django 4.0.7 on 2022-10-13 13:33

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='descricao',
            field=tinymce.models.HTMLField(verbose_name='Descrição'),
        ),
    ]
