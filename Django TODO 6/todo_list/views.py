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

