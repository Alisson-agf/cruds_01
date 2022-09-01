from django.forms import ModelForm
from .models import Professor, Motorista, Informatica


class ProfessorForm(ModelForm):
    class Meta:
           model = Professor
           fields = ['nome', 'email', 'dataNasci']

class MotoristaForm(ModelForm):
    class Meta:
           model = Motorista
           fields = ['nome', 'email', 'dataNasci']

class InformaticaForm(ModelForm):
    class Meta:
           model = Informatica
           fields = ['nome', 'email', 'dataNasci']

