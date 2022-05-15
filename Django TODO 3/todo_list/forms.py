from django import forms
from django.forms import ModelForm
from .models import Task

class TodoTaskForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task here...', 'background-color': 'blue'}))

    class Meta:
        model = Task
        fields = "__all__"