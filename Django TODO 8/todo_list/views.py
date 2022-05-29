from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TodoForm

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

def about(request):
    return HttpResponse("<h1>About Page</h1>")
