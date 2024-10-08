# Generated by Django 4.2.13 on 2024-07-08 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=194, verbose_name='Nome do vendedor')),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=12)),
                ('cidade', models.CharField(blank=True, max_length=10)),
                ('estado', models.CharField(blank=True, choices=[('acre', 'Acre'), ('alagoas', 'Alagoas'), ('amazonas', 'Amazonas'), ('bahia', 'Bahia'), ('ceara', 'Ceará'), ('distriito federal', 'Distrito Federal'), ('espirito santo', 'Espirito Santos'), ('goias', 'Goias'), ('maranhão', 'Maranhão'), ('mato grosso', 'Mato Grosso'), ('palmas', 'Palmas'), ('parana', 'Paraná'), ('pernambudo', 'Pernambuco'), ('piaui', 'Piaui'), ('sergipe', 'Sergipe'), ('sao paulo', 'São Paulo'), ('rio de janeiro', 'Rio de Janeiro')], max_length=20)),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
                'db_table': 'contato',
            },
        ),
    ]
