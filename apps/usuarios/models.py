from django.db import models
import re
from django.contrib.auth.models import(
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None):
        usuario = self.model(email=self.normalize_email(email))
        
        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)

        usuario.save()

        return usuario
    
    def create_superuser(self, email, password):
        usuario = self.create_user(
            email=self.normalize_email(email),
            password = password,
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()

        return usuario

"""Função de validação de CPF do usuário
def validar_cpf(value):
    if not re.match(r'ˆ\d{11}$', value):
        raise ValidationError("CPF deve ter 11 dígitos númericos.")
"""



class Usuario(AbstractBaseUser, PermissionsMixin):

    SETOR = [
        ('Comercial', 'Comercial'),
        ('Marketing', 'MArketing'),
        ('Financeiro', 'Financeiro'),
        ('Outros', 'Outros'),
    ]

    nome_completo = models.CharField(
        verbose_name="Nome completo", 
        max_length=200,
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
        unique=True,
    )


    email = models.EmailField(
        verbose_name="E-mail do usuário", 
        max_length=194, 
        unique=True
    )

    foto_perfil = models.FileField(
        upload_to="Imagem perfil/", 
        blank=True
    )

    telefone = models.CharField(
        blank=True,
        max_length=12
    )

    cidade = models.CharField(
        max_length=20,
        blank=True
    )

    estado = models.CharField(
        max_length=20,
        blank=True
    )

    funcao = models.CharField(
        max_length=20,
        blank=True,
        choices=SETOR
    )


    is_active = models.BooleanField(verbose_name="Usuário está ativo", default=True)

    is_staff = models.BooleanField(verbose_name="Usuário é da equipe", default=False)

    is_superuser = models.BooleanField(verbose_name="Super usuário", default=False)

    USERNAME_FIELD = "email"

    objects = UsuarioManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        db_table = "usuario"


    def __str__(self):
        return self.email