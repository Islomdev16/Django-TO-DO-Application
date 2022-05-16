from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoTask
from .forms import TodoTaskForm

def tasks(request):
    lists = TodoTask.objects.all().order_by('-created')

    form = TodoTaskForm()
    if request.method == 'POST':
        form = TodoTaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("tasks")
    context = {
        'lists': lists,
        'form':form
    }
    return render(request, 'index.html', context)


def updateTask(request, pk):
    task = TodoTask.objects.get(id=pk)
    form = TodoTaskForm(instance=task)
    if request.method == 'POST':
        form = TodoTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("tasks")

    context = {
        'form':form
    }
    return render(request, 'update_task.html', context)


def deleteTask(request, pk):
    item = TodoTask.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect("tasks")

    context = {
        'item': item
    }
    return render(request, 'delete_task.html', context)
