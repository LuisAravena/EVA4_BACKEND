from django import forms
from .models import Numero

class NumeroForm(forms.ModelForm):
    class Meta:
        model = Numero
        fields = ['numero', 'es_spam']
