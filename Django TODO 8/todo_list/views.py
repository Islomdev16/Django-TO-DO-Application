from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TodoForm

# Create your views here.
def index(request):
    todos = Task.objects.all()
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
        'form': form
    }
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("<h1>About Page</h1>")
