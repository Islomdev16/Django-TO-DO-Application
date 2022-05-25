from django.shortcuts import render
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

