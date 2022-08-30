from django.db import models

class Curso(models.Model):
    titulo = models.CharField('Nome:', max_length=100)
    vagas = models.IntegerField('Profissão:')
