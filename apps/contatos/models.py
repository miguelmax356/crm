from django.db import models

from cadastro_seller.models import Oportunidade, Empresa
from usuarios.models import Usuario


class Contato(models.Model):

    ESTADOS_CHOICES = [
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

    negocio = models.ForeignKey(Oportunidade, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nome = models.CharField(max_length=194)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=12,)
    cargo = models.CharField(max_length=20, blank=True, null=True)
    cidade = models.CharField(max_length=10, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES, blank=True, null=True)
    responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)


    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
        db_table = "contato"
    

    def __str__(self):
        return self.nome


################################## Tarefas a partir daqui ###############################

