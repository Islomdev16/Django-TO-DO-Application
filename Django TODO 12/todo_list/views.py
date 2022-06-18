from django.shortcuts import render, redirect
from .models import MyTodo

# Create your views here.
def home(request):
    count_tasks = MyTodo.objects.all().count()
    if request.method == 'POST':
        title = request.POST.get('title')
        if title != '':
            MyTodo.objects.create(title=title)
        return redirect('home')
    tasks = MyTodo.objects.all().order_by("complete", '-created_at')
    context = {
        'tasks':tasks,
        'count_tasks':count_tasks,
    }
    return render(request, 'home.html', context)

def delete_task(request, pk):
    task_delete = MyTodo.objects.get(id=pk)
    task_delete.delete()
    return redirect('home')

def complete(request, pk):
    data = MyTodo.objects.get(id=pk)
    data.complete = True
    data.save()
    return redirect('home')

def uncomplete(request, pk):
    data = MyTodo.objects.get(id=pk)
    data.complete = False
    data.save()
    return redirect('home')

