from django.shortcuts import render
from .models import MyTodo

# Create your views here.
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        MyTodo.objects.create(title=title)
    tasks = MyTodo.objects.all().order_by("complete", '-created_at')
    context = {
        'tasks':tasks
    }
    return render(request, 'home.html', context)
