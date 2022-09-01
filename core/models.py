from django.db import models

class Emprego(models.Model):
    identidade = models.CharField('Nome:', max_length=100)
    especialidade = models.IntegerField('Profissão:')

