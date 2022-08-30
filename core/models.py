from django.db import models

class Curso(models.Model):
<<<<<<< HEAD
    titulo = models.CharField('Nome:', max_length=100)
    vagas = models.IntegerField('Profissão:')
=======
    profissão = models.CharField('Profissão', max_length=100)
    vagas = models.IntegerField('Vagas')
>>>>>>> 2e5c034149b2cbe1b54143533e8bfdbb3ebdf5ab
