from django import forms
from .models import Mytodo

class TodoForm(forms.ModelForm):
    task = forms.CharField(max_length=50, widget=forms.TextInput(attrs={}))
    class Meta:
        model = Mytodo
        fields = "__all__"

