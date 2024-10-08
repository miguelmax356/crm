# Generated by Django 4.2.13 on 2024-07-08 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(blank=True, max_length=300)),
                ('cnpj', models.CharField(max_length=14)),
                ('endereco', models.CharField(blank=True, max_length=300)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('TO', 'Tocantins'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('RJ', 'Rio de Janeiro')], max_length=2)),
                ('telefone', models.CharField(max_length=11)),
                ('classificacao', models.CharField(choices=[('bronze', 'Bronze'), ('prata', 'Prata'), ('ouro', 'Ouro')], max_length=6)),
                ('segmento', models.CharField(choices=[('Móveis & Eletro', 'Móveis & Eletro'), ('Supermercado', 'Supermercado'), ('Petshop', 'Petshop'), ('Automotivo', 'Automotivo'), ('Vestuário', 'Vestuário'), ('Cosmético', 'Cosméticos'), ('Brinquedo', 'Brinquedo'), ('Smartphone', 'Smartphone'), ('Home Center', 'Home Center'), ('Baby', 'Baby'), ('Papelaria', 'Papelaria')], max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('banco', models.CharField(blank=True, choices=[('caixa economica', 'Caixa Econômica'), ('banco do brasil', 'Banco do Brasil'), ('bradesco', 'Bradesco'), ('itau', 'Itaú')], max_length=20, verbose_name='Banco')),
                ('agencia', models.CharField(blank=True, max_length=5)),
                ('conta', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'db_table': 'empresa',
            },
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=194, verbose_name='Empresa')),
                ('contato_lead', models.CharField(max_length=50, verbose_name='Nome do contato')),
                ('email_lead', models.EmailField(blank=True, max_length=254)),
                ('telefone_lead', models.CharField(max_length=11)),
                ('endereco_lead', models.CharField(blank=True, max_length=194, verbose_name='Endereço')),
                ('qualificacao_lead', models.CharField(choices=[('bronze', 'Bronze'), ('prata', 'Prata'), ('ouro', 'Ouro')], max_length=6)),
                ('cnpj_lead', models.CharField(max_length=14)),
                ('segmento', models.CharField(choices=[('Móveis & Eletro', 'Móveis & Eletro'), ('Supermercado', 'Supermercado'), ('Petshop', 'Petshop'), ('Automotivo', 'Automotivo'), ('Vestuário', 'Vestuário'), ('Cosmético', 'Cosméticos'), ('Brinquedo', 'Brinquedo'), ('Smartphone', 'Smartphone'), ('Home Center', 'Home Center'), ('Baby', 'Baby'), ('Papelaria', 'Papelaria')], max_length=20)),
            ],
            options={
                'verbose_name': 'Lead',
                'verbose_name_plural': 'Leads',
                'db_table': 'lead',
            },
        ),
        migrations.CreateModel(
            name='Oportunidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('taxa_comissao', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Taxa de Comissão')),
                ('status_negociacao', models.CharField(choices=[('em negociacao', 'Em negociação'), ('ganha', 'Ganha'), ('perdida', 'Perdida'), ('cancelada', 'Cancelada')], max_length=30, verbose_name='Status da Oportunidade')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_fechamento', models.DateTimeField(verbose_name='Data de fechamento')),
                ('probabilidade', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Probabilidade')),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='Termos de parceria/')),
            ],
            options={
                'verbose_name': 'Oportunidade',
                'verbose_name_plural': 'Oportunidades',
                'db_table': 'oportunidade',
            },
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atividade', models.CharField(choices=[('Ligacao', 'Ligação'), ('Email', 'E-mail'), ('Visita', 'Visita'), ('Online', 'Online')], max_length=7)),
                ('telefone', models.CharField(max_length=11)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('descricao', models.CharField(max_length=300)),
                ('status', models.CharField(blank=True, choices=[('Nova', 'Nova'), ('Em andamento', 'Em andamento'), ('Concluida', 'Concluída')], max_length=13)),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Criação da tarefa')),
                ('contato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contatos', to='contatos.contato')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarefas', to='cadastro_seller.empresa')),
                ('oportunidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarefas', to='cadastro_seller.oportunidade')),
            ],
            options={
                'verbose_name': 'Tarefa',
                'verbose_name_plural': 'Tarefas',
                'db_table': 'tarefa',
            },
        ),
    ]
