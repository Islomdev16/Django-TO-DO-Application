from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'index.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'detail.html'

class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    # context_object_name = 'task_create'
    template_name = 'create_task.html'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    template_name = 'create_task.html'
    # template_name = 'create_task.html'
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    fields = "__all__"
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('tasks')
