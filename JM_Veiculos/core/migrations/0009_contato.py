# Generated by Django 4.2.4 on 2023-10-04 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_carro_placa_moto_placa_utilitarios_placa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=255)),
                ('mensagem', models.TextField()),
            ],
        ),
    ]