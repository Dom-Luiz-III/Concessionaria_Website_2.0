# Generated by Django 4.2.4 on 2023-10-02 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_carro_situacao_moto_situacao_utilitarios_situacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='placa',
            field=models.CharField(default='BRA2E19', max_length=7, verbose_name='placa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moto',
            name='placa',
            field=models.CharField(default='BRA2E19', max_length=7, verbose_name='placa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='utilitarios',
            name='placa',
            field=models.CharField(default='BRA2E19', max_length=7, verbose_name='placa'),
            preserve_default=False,
        ),
    ]
