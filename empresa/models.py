from django.db import models

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    endereso = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
