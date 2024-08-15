from django.db import models
from usuarios.models import Usuario



class Empresa(models.Model):
    RELEVANCIA = [
        ('Bronze', 'Bronze'),
        ('Prata', 'Prata'),
        ('Ouro', 'Ouro'),
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
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    endereco = models.CharField(max_length=300, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=2, choices=ESTADOS, blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    classificacao = models.CharField(max_length=6, choices=RELEVANCIA, blank=True, null=True)
    segmento = models.CharField(max_length=20, choices=SEGMENTOS, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    banco = models.CharField(verbose_name="Banco", max_length=20, choices=BANCOS, blank=True, null=True)
    agencia = models.CharField(max_length=5, blank=True, null=True)
    conta = models.CharField(max_length=20, blank=True, null=True)


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
    taxa_comissao = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Taxa de Comissão")
    status_negociacao = models.CharField(max_length=30, verbose_name="Status do Negócio", choices=STATUS)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_fechamento = models.DateTimeField(verbose_name="Data de fechamento")
    probabilidade = models.DecimalField(max_digits=3, decimal_places=0, verbose_name="Probabilidade")
    arquivo = models.FileField(upload_to="Termos de parceria/", null=True, blank=True)


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
        ('Reunião Online', 'Reunião Online'),
        ('Whatsapp', 'Whatsapp'),
    ]

    STATUS_TAREFA = [
        ('Prospecção', 'Prospecção'),
        ('Aguardando Apresentação', 'Aguardando Apresentação'),
        ('Aguardando Reunião', 'Aguardando Reunião'),
        ('Em negociação', 'Em negociação'),
        ('Concluida', 'Concluída'),
    ]

    contato = models.ForeignKey('contatos.Contato', on_delete=models.CASCADE)
    negocio = models.ForeignKey(Oportunidade, on_delete=models.CASCADE, related_name="tarefas")
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, related_name="empresa_tarefa")
    atividade = models.CharField(max_length=14, choices=TIPO_TAREFA)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(blank=True)
    descricao = models.CharField(max_length=300)
    status = models.CharField(max_length=23, blank=True, choices=STATUS_TAREFA)
    data_inicio = models.DateField(blank=True, null=True)
    horario_inicio = models.TimeField(blank=True, null=True)
    data_fim = models.DateTimeField(blank=True, null=True)
    horario_fim = models.TimeField(blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="tarefas")


    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        db_table = "tarefa"

    def __str__(self):
        return self.atividade


class Lead(models.Model):
    RELEVANCIA = [
        ('Bronze', 'Bronze'),
        ('Prata', 'Prata'),
        ('Ouro', 'Ouro'),
    ]

    SEGMENTOS = [
        ('Artigos Religiosos', 'Artigos Religiosos'),
        ('Automotivo', 'Automotivo'),
        ('Baby', 'Baby'),
        ('Brinquedo', 'Brinquedo'),
        ('Cosmético', 'Cosméticos'),
        ('Home Center', 'Home Center'),
        ('Itens Esportivos', 'Itens Esportivos'),
        ('Móveis & Eletro', 'Móveis & Eletro'),
        ('Papelaria', 'Papelaria'),
        ('Petshop', 'Petshop'),
        ('Smartphone', 'Smartphone'),
        ('Supermercado', 'Supermercado'),
        ('Vestuário', 'Vestuário'),
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
