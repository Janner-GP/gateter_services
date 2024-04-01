from typing import Any
from django import forms
from .models import Meow

class MeowsForm(forms.ModelForm):
    class Meta:
        model = Meow
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control text-bg-dark'}),
            'text': forms.Textarea(attrs={'class': 'form-control text-bg-dark'}),
        }