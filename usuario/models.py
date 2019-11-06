from django.db import models

# Create your models here.

class usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255) 
    senha = models.CharField(max_length=255) 
    numero = models.CharField(max_length=255)
    nacimento = models.CharField(max_length=255)
