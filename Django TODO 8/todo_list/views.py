from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TodoForm, UpdateForm

# Create your views here.
def index(request):
    todos = Task.objects.all()
    count_todos = todos.count()
    completed_todo = Task.objects.filter(complete=True)
    count_completed_todo = completed_todo.count()
    count_uncompleted_todo = count_todos - count_completed_todo

    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = TodoForm()

    context = {
        'todos': todos,
        'form': form,
        'count_todos': count_todos,
        'count_completed_todo': count_completed_todo,
        'count_uncompleted_todo': count_uncompleted_todo
    }
    return render(request, 'index.html', context)

def update(request, pk):
    todo = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UpdateForm(instance=todo)

    context = {
        'form': form
    }
    return render(request, 'update.html', context)
