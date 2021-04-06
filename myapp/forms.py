from django import forms
from myapp.models import myapp

class empforms(forms.ModelForm):
    class Meta:
        model=myapp
        fields="__all__"