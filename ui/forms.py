from django import forms 
from .models import CodeModels

class CodeForm(forms.ModelForm):
    class Meta:
        model =  CodeModels
        fields = ["name", "code"]
