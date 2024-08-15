# Generated by Django 4.2.13 on 2024-08-15 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_seller', '0021_alter_oportunidade_status_negociacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='agencia',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='bairro',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='banco',
            field=models.CharField(blank=True, choices=[('caixa economica', 'Caixa Econômica'), ('banco do brasil', 'Banco do Brasil'), ('bradesco', 'Bradesco'), ('itau', 'Itaú')], max_length=20, null=True, verbose_name='Banco'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='cidade',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='classificacao',
            field=models.CharField(blank=True, choices=[('Bronze', 'Bronze'), ('Prata', 'Prata'), ('Ouro', 'Ouro')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='cnpj',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='conta',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='endereco',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='estado',
            field=models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('TO', 'Tocantins'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('RJ', 'Rio de Janeiro')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='segmento',
            field=models.CharField(blank=True, choices=[('Móveis & Eletro', 'Móveis & Eletro'), ('Supermercado', 'Supermercado'), ('Petshop', 'Petshop'), ('Automotivo', 'Automotivo'), ('Vestuário', 'Vestuário'), ('Cosmético', 'Cosméticos'), ('Brinquedo', 'Brinquedo'), ('Smartphone', 'Smartphone'), ('Home Center', 'Home Center'), ('Baby', 'Baby'), ('Papelaria', 'Papelaria')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='telefone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='qualificacao_lead',
            field=models.CharField(choices=[('Bronze', 'Bronze'), ('Prata', 'Prata'), ('Ouro', 'Ouro')], max_length=6),
        ),
        migrations.AlterField(
            model_name='lead',
            name='segmento',
            field=models.CharField(choices=[('Artigos Religiosos', 'Artigos Religiosos'), ('Automotivo', 'Automotivo'), ('Baby', 'Baby'), ('Brinquedo', 'Brinquedo'), ('Cosmético', 'Cosméticos'), ('Home Center', 'Home Center'), ('Itens Esportivos', 'Itens Esportivos'), ('Móveis & Eletro', 'Móveis & Eletro'), ('Papelaria', 'Papelaria'), ('Petshop', 'Petshop'), ('Smartphone', 'Smartphone'), ('Supermercado', 'Supermercado'), ('Vestuário', 'Vestuário')], max_length=20),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='atividade',
            field=models.CharField(choices=[('Ligacao', 'Ligação'), ('Email', 'E-mail'), ('Visita', 'Visita'), ('Reunião Online', 'Reunião Online'), ('Whatsapp', 'Whatsapp')], max_length=14),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='status',
            field=models.CharField(blank=True, choices=[('Prospecção', 'Prospecção'), ('Aguardando Apresentação', 'Aguardando Apresentação'), ('Aguardando Reunião', 'Aguardando Reunião'), ('Em negociação', 'Em negociação'), ('Concluida', 'Concluída')], max_length=23),
        ),
    ]
