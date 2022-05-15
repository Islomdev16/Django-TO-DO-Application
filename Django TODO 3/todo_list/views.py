from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TodoTaskForm

def home(request):
    context = {"success": False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Task(title=title, description=desc)
        ins.save()
        context = {
            "success": True,
            "title":title
        }



    return render(request, 'index.html', context)

def tasks(request):
    all_tasks = Task.objects.all().order_by("-time")
    context = {"tasks":all_tasks}
    return render(request, 'tasks.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
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
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect("tasks")

    context = {
        'item': item
    }
    return render(request, 'delete_task.html', context)