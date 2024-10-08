# Generated by Django 4.2.13 on 2024-07-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_seller', '0016_remove_tarefa_data_tarefa_data_inicio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefa',
            name='empresa',
        ),
        migrations.AddField(
            model_name='tarefa',
            name='horario_fim',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='horario_incio',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='data_inicio',
            field=models.DateField(blank=True, null=True),
        ),
    ]
