from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Task title ...'}))
    due = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Due date ...'}))

    class Meta:
        model = Task
        fields = ['title', 'due']


class UpdateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Task title ...'}))

    class Meta:
        model = Task
        fields = ['title', 'due', 'complete']
