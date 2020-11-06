from django import forms
from .models import Bb


class BbForm(forms.ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric', 'kind')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
