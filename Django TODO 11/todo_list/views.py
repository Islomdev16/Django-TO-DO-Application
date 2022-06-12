from django.shortcuts import render, redirect
from .forms import TaskForm, UpdateForm
from .models import Task

def homeTask(request):
    tasks = Task.objects.all().order_by('complete', '-due')
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {
        'tasks':tasks,
        'form':form
    }
    return render(request, 'index.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = UpdateForm(instance=task)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {
        'task':task,
        'form':form
    }
    return render(request, 'update_task.html', context)