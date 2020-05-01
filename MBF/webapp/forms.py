from django import forms
from webapp.models import EMPMODEL
class myform(forms.ModelForm):
    class Meta:
        model=EMPMODEL
        fields='__all__'