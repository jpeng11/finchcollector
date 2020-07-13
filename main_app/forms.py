from django.forms import ModelForm
from .models import Last

class SeenForm(ModelForm):
  class Meta:
    model = Last
    fields = ['date', 'time']