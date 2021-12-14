from django.forms import ModelForm

from .models import Licnoe_delo

class Licnoe_deloForm(ModelForm):
  class Meta:
     model = Licnoe_delo
     fields = ('fio', 'number_dela', 'education', 'qualification', 'data_priema', 'dolya', 'hours_worked', 'amount_to_issue')

