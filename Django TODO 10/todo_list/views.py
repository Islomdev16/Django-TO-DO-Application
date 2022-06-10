from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'detail.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = "__all__"
    # context_object_name = 'task_create'
    template_name = 'create_task.html'
    success_url = reverse_lazy('tasks')

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = "__all__"
    template_name = 'create_task.html'
    # template_name = 'create_task.html'
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = "__all__"
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('tasks')

class UserLoginView(LoginView):
    template_name = 'login.html'
    fields = "__all__"
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('tasks')
