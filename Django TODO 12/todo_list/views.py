from django.shortcuts import render
from .models import MyTodo

# Create your views here.
def home(request):
    tasks = MyTodo.objects.all().order_by('-created_at')
    context = {
        'tasks':tasks
    }
    return render(request, 'home.html', context)
