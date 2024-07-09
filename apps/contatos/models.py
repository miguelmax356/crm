from django.db import models



class Contato(models.Model):

    ESTADOS_CHOICES  = [
        ('acre', 'Acre'),
        ('alagoas', 'Alagoas'),
        ('amazonas', 'Amazonas'),
        ('bahia', 'Bahia'),
        ('ceara', 'Ceará'),
        ('distriito federal', 'Distrito Federal'),
        ('espirito santo', 'Espirito Santos'),
        ('goias', 'Goias'),
        ('maranhão', 'Maranhão'),
        ('mato grosso', 'Mato Grosso'),
        ('palmas', 'Palmas'),
        ('parana', 'Paraná'),
        ('pernambudo', 'Pernambuco'),
        ('piaui', 'Piaui'),
        ('sergipe', 'Sergipe'),
        ('sao paulo', 'São Paulo'),
        ('rio de janeiro', 'Rio de Janeiro'),

    ]

    nome_completo = models.CharField(verbose_name="Nome do vendedor", max_length=194)
    email = models.EmailField()
    telefone = models.CharField(max_length=12)
    cidade = models.CharField(max_length=10, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES, blank=True)


    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
        db_table = "contato"
    
    def __str__(self):
        return self.nome_completo
