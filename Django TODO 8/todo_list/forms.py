from django import forms
from .models import Task

class TodoForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Add new task here ..."}))

    class Meta:
        model = Task
        fields = ['content']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
