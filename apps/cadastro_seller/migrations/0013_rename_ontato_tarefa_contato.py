# Generated by Django 4.2.13 on 2024-07-11 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_seller', '0012_tarefa_ontato'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='ontato',
            new_name='contato',
        ),
    ]
