from django.forms import ModelForm
from .models import Emprego


class EmpregoForm(ModelForm):
    class Meta:
           model = Emprego
           fields = ['titulo', 'vagas']
