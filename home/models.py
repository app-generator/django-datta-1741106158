# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Alunos(models.Model):

    #__Alunos_FIELDS__
    cgm = models.IntegerField(null=True, blank=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    data_nasc = models.DateTimeField(blank=True, null=True, default=timezone.now)
    contato = models.CharField(max_length=255, null=True, blank=True)
    filiacao1 = models.CharField(max_length=255, null=True, blank=True)
    filiacao2 = models.CharField(max_length=255, null=True, blank=True)
    responsavel = models.CharField(max_length=255, null=True, blank=True)
    contatos = models.CharField(max_length=255, null=True, blank=True)
    matricula = models.CharField(max_length=255, null=True, blank=True)

    #__Alunos_FIELDS__END

    class Meta:
        verbose_name        = _("Alunos")
        verbose_name_plural = _("Alunos")


class Responsavel(models.Model):

    #__Responsavel_FIELDS__
    cpf_resp = models.CharField(max_length=255, null=True, blank=True)
    endereco_resp = models.TextField(max_length=255, null=True, blank=True)
    tipo_parentesco = models.CharField(max_length=255, null=True, blank=True)

    #__Responsavel_FIELDS__END

    class Meta:
        verbose_name        = _("Responsavel")
        verbose_name_plural = _("Responsavel")


class Filiacao1(models.Model):

    #__Filiacao1_FIELDS__
    cpf_filiacao1 = models.CharField(max_length=255, null=True, blank=True)
    contato_filiacao1 = models.CharField(max_length=255, null=True, blank=True)
    endereco_filiacao1 = models.TextField(max_length=255, null=True, blank=True)

    #__Filiacao1_FIELDS__END

    class Meta:
        verbose_name        = _("Filiacao1")
        verbose_name_plural = _("Filiacao1")


class Filiacao2(models.Model):

    #__Filiacao2_FIELDS__
    endereco_filiacao2 = models.TextField(max_length=255, null=True, blank=True)

    #__Filiacao2_FIELDS__END

    class Meta:
        verbose_name        = _("Filiacao2")
        verbose_name_plural = _("Filiacao2")


class Unidade(models.Model):

    #__Unidade_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    dados_gerais = models.TextField(max_length=255, null=True, blank=True)

    #__Unidade_FIELDS__END

    class Meta:
        verbose_name        = _("Unidade")
        verbose_name_plural = _("Unidade")


class Ano_Letivo(models.Model):

    #__Ano_Letivo_FIELDS__
    ano = models.CharField(max_length=255, null=True, blank=True)
    data_inicio = models.DateTimeField(blank=True, null=True, default=timezone.now)
    data_fim = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.BooleanField()

    #__Ano_Letivo_FIELDS__END

    class Meta:
        verbose_name        = _("Ano_Letivo")
        verbose_name_plural = _("Ano_Letivo")


class Turmas(models.Model):

    #__Turmas_FIELDS__
    max_alunos = models.IntegerField(null=True, blank=True)
    ano_letivo = models.IntegerField(null=True, blank=True)
    turno = models.CharField(max_length=255, null=True, blank=True)

    #__Turmas_FIELDS__END

    class Meta:
        verbose_name        = _("Turmas")
        verbose_name_plural = _("Turmas")


class Matricula(models.Model):

    #__Matricula_FIELDS__
    status = models.CharField(max_length=255, null=True, blank=True)
    data_matricula = models.DateTimeField(blank=True, null=True, default=timezone.now)
    unid_origem = models.CharField(max_length=255, null=True, blank=True)
    unid_destino = models.CharField(max_length=255, null=True, blank=True)
    data_saida = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Matricula_FIELDS__END

    class Meta:
        verbose_name        = _("Matricula")
        verbose_name_plural = _("Matricula")


class Funcionarios(models.Model):

    #__Funcionarios_FIELDS__
    data_inicio = models.DateTimeField(blank=True, null=True, default=timezone.now)
    data_saida = models.DateTimeField(blank=True, null=True, default=timezone.now)
    cargo = models.CharField(max_length=255, null=True, blank=True)
    funcao = models.CharField(max_length=255, null=True, blank=True)
    tipo = models.CharField(max_length=255, null=True, blank=True)
    cpf_func = models.CharField(max_length=255, null=True, blank=True)
    rg_func = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    endereco = models.TextField(max_length=255, null=True, blank=True)
    contato = models.CharField(max_length=255, null=True, blank=True)

    #__Funcionarios_FIELDS__END

    class Meta:
        verbose_name        = _("Funcionarios")
        verbose_name_plural = _("Funcionarios")



#__MODELS__END
