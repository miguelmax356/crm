from django.db import models
from contatos.models import Contato
from usuarios.models import Usuario

class Empresa(models.Model):
    RELEVANCIA = [
        ('bronze', 'Bronze'),
        ('prata', 'Prata'),
        ('ouro', 'Ouro'),
    ]

    ESTADOS = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('TO', 'Tocantins'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('RJ', 'Rio de Janeiro'),
    ]

    SEGMENTOS = [
        ('Móveis & Eletro', 'Móveis & Eletro'),
        ('Supermercado', 'Supermercado'),
        ('Petshop', 'Petshop'),
        ('Automotivo', 'Automotivo'),
        ('Vestuário', 'Vestuário'),
        ('Cosmético', 'Cosméticos'),
        ('Brinquedo', 'Brinquedo'),
        ('Smartphone', 'Smartphone'),
        ('Home Center', 'Home Center'),
        ('Baby', 'Baby'),
        ('Papelaria', 'Papelaria'),
    ]

    BANCOS = [
        ('caixa economica', 'Caixa Econômica'),
        ('banco do brasil', 'Banco do Brasil'),
        ('bradesco', 'Bradesco'),
        ('itau', 'Itaú'),
    ]

    vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="responsavel")
    empresa = models.CharField(max_length=300, blank=True)
    cnpj = models.CharField(max_length=14)
    endereco = models.CharField(max_length=300, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=ESTADOS)
    telefone = models.CharField(max_length=11)
    classificacao = models.CharField(max_length=6, choices=RELEVANCIA)
    segmento = models.CharField(max_length=20, choices=SEGMENTOS)
    email = models.EmailField()
    banco = models.CharField(verbose_name="Banco", max_length=20, choices=BANCOS, blank=True)
    agencia = models.CharField(max_length=5, blank=True)
    conta = models.CharField(max_length=20, blank=True)


    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        db_table = "empresa"

    def __str__(self):
        return self.empresa


class Oportunidade(models.Model):
    STATUS = [
        ('em negociacao', 'Em negociação'),
        ('ganha', 'Ganha'),
        ('perdida', 'Perdida'),
        ('cancelada', 'Cancelada'),
    ]

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="oportunidades")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="vendas")
    titulo = models.CharField(max_length=200)
    taxa_comissao = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Taxa de Comissão")
    status_negociacao = models.CharField(max_length=30, verbose_name="Status da Oportunidade", choices=STATUS)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_fechamento = models.DateTimeField(verbose_name="Data de fechamento")
    probabilidade = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Probabilidade")
    arquivo = models.FileField(upload_to="Termos de parceria/", null=True, blank=True)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE, related_name="contato", blank=True)

    class Meta:
        verbose_name = "Oportunidade"
        verbose_name_plural = "Oportunidades"
        db_table = "oportunidade"

    def __str__(self):
        return self.titulo


class Tarefa(models.Model):
    TIPO_TAREFA = [
        ('Ligacao', 'Ligação'),
        ('Email', 'E-mail'),
        ('Visita', 'Visita'),
        ('Online', 'Online')
    ]

    STATUS_TAREFA = [
        ('Nova', 'Nova'),
        ('Em andamento', 'Em andamento'),
        ('Concluida', 'Concluída'),
    ]

    oportunidade = models.ForeignKey(Oportunidade, on_delete=models.CASCADE, related_name="tarefas")
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, related_name="empresa_tarefa")
    atividade = models.CharField(max_length=7, choices=TIPO_TAREFA)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE, related_name="contatos")
    telefone = models.CharField(max_length=11)
    email = models.EmailField(blank=True)
    descricao = models.CharField(max_length=300)
    status = models.CharField(max_length=13, blank=True, choices=STATUS_TAREFA)
    data = models.DateTimeField(verbose_name="Criação da tarefa", auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="tarefas")

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        db_table = "tarefa"

    def __str__(self):
        return self.atividade


class Lead(models.Model):
    RELEVANCIA = [
        ('bronze', 'Bronze'),
        ('prata', 'Prata'),
        ('ouro', 'Ouro'),
    ]

    SEGMENTOS = [
        ('Móveis & Eletro', 'Móveis & Eletro'),
        ('Supermercado', 'Supermercado'),
        ('Petshop', 'Petshop'),
        ('Automotivo', 'Automotivo'),
        ('Vestuário', 'Vestuário'),
        ('Cosmético', 'Cosméticos'),
        ('Brinquedo', 'Brinquedo'),
        ('Smartphone', 'Smartphone'),
        ('Home Center', 'Home Center'),
        ('Baby', 'Baby'),
        ('Papelaria', 'Papelaria'),
    ]

    nome_empresa = models.CharField(verbose_name="Empresa", max_length=194)
    contato_lead = models.CharField(verbose_name="Nome do contato", max_length=50)
    email_lead = models.EmailField(blank=True)
    telefone_lead = models.CharField(max_length=11)
    endereco_lead = models.CharField(verbose_name="Endereço", max_length=194, blank=True)
    qualificacao_lead = models.CharField(choices=RELEVANCIA, max_length=6)
    cnpj_lead = models.CharField(max_length=14)
    vendedor_lead = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, related_name="leads")
    segmento = models.CharField(max_length=20, choices=SEGMENTOS)

    def converter_para_empresa(self):
        return Empresa(
            vendedor=self.vendedor_lead,
            empresa=self.nome_empresa,
            cnpj=self.cnpj_lead,
            endereco=self.endereco_lead,
            telefone=self.telefone_lead,
            email=self.email_lead,
            segmento=self.segmento,
        )

    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Leads"
        db_table = "lead"

    def __str__(self):
        return self.nome_empresa
