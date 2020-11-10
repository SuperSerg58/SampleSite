from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task'}))

    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'complete': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }