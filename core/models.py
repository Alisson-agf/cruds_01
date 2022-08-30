from django.db import models
####carneiro ###
class Emprego(models.Model):
    titulo = models.CharField('Nome:', max_length=100)
    vagas = models.IntegerField('Profissão:')

