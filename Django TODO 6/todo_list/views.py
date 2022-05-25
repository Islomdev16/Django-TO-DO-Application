from django.shortcuts import render, redirect
from .models import Mytodo
from .forms import TodoForm

# Create your views here.
def home(request):
    tasks = Mytodo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'index.html', context)

def delete_task(request, pk):
    task = Mytodo.objects.get(id=pk)
    task.delete()
    return redirect('all_tasks')

def update_task(request, pk):
    todo = Mytodo.objects.get(id=pk)
    updateForm = TodoForm(instance=todo)
    if request.method == 'POST':
        updateForm = TodoForm(request.POST, instance=todo)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('all_tasks')

    context = {
        'todo':todo,
        'update_form':updateForm
    }
    return render(request, 'update.html', context)

