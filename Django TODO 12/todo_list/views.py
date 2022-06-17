from django.shortcuts import render, redirect
from .models import MyTodo

# Create your views here.
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title != '':
            MyTodo.objects.create(title=title)
        return redirect('home')
    tasks = MyTodo.objects.all().order_by("complete", '-created_at')
    context = {
        'tasks':tasks
    }
    return render(request, 'home.html', context)
