# Generated by Django 4.2.13 on 2024-07-13 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_seller', '0020_rename_oportunidade_tarefa_negocio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oportunidade',
            name='status_negociacao',
            field=models.CharField(choices=[('em negociacao', 'Em negociação'), ('ganha', 'Ganha'), ('perdida', 'Perdida'), ('cancelada', 'Cancelada')], max_length=30, verbose_name='Status do Negócio'),
        ),
    ]
