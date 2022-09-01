from django.db import models

class Professor(models.Model):
    nome = models.CharField('Nome', max_length=255)
    email = models.EmailField('Email')
    dataNasci= models.DateField('Data de Nascimento')

class Motorista(models.Model):
    nome = models.CharField('Nome', max_length=255)
    email = models.EmailField('Email')
    dataNasci= models.DateField('Data de Nascimento')

class Informatica(models.Model):
    nome = models.CharField('Nome', max_length=255)
    email = models.EmailField('Email')
    dataNasci= models.DateField('Data de Nascimento')



