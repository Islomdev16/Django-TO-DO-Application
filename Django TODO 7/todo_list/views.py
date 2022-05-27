from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def home(request):
    tasks = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = TodoForm()

    context = {
        'tasks':tasks,
        'form':form
    }
    return render(request, 'home.html', context)

def delete_task(request, pk):
    task = Todo.objects.get(id=pk)
    task.delete()
    return redirect('home')

