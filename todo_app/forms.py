from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(
        label= 'tarea',
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'task-control'})
    )
    class Meta:
        model = Task
        fields = ['title']
    
