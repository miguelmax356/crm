# Generated by Django 4.2.13 on 2024-07-12 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_seller', '0017_remove_tarefa_empresa_tarefa_horario_fim_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='empresa',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='empresa_tarefa', to='cadastro_seller.empresa'),
            preserve_default=False,
        ),
    ]
