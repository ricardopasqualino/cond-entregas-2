from curses import flash
from email.policy import default
from sys import maxsize
from unicodedata import numeric
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


class Morador(models.Model):
    nome = models.CharField(max_length=200, default=None, null=True)
    sobrenome = models.CharField(max_length=200, default=None, null=True)
    telefone = models.CharField(max_length=40, default=None, null=True)
    email = models.CharField(max_length=200, default=None, null=True)
    aceite_alertas = models.BooleanField(default=False) #Morador configurado para receber alertas


    def __str__(self):
        return self.nome


class Casa(models.Model):
    numero = models.CharField(max_length=3, default=None, null=True)
    rua = models.CharField(max_length=200, default=None, null=True)
    moradores = models.ForeignKey(Morador, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    # pessoa = models.ManyToManyField(Morador, default=None)


    def __str__(self):
        return self.numero


class Box(models.Model):
    box = models.CharField(max_length=10, default=None, null=False)

    def __str__(self):
        return self.box


class Delivery(models.Model):
    nota_fiscal = models.CharField(max_length=6, default=None, null=False, blank=False)
    casa = models.ForeignKey(Casa, on_delete=models.DO_NOTHING, default=Casa, auto_created=True)
    data_entrada = models.DateTimeField(null=False, blank=False, auto_now=True, unique_for_date=True)
    modulo = models.ForeignKey(Box, on_delete=models.SET_NULL, default=Box, null=True)
    recebido_por = models.ForeignKey(User, on_delete=models.SET_NULL, default=User, null=True) 
    status = models.BooleanField(null=False, default=False)


    def __str__(self):
        return self.nota_fiscal


class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15, default=None, null=True)

    def __str__(self):
        return self.usuario
