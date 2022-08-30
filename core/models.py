from django.db import models

class Curso(models.Model):
    profissão = models.CharField('Profissão', max_length=100)
    vagas = models.IntegerField('Vagas')
