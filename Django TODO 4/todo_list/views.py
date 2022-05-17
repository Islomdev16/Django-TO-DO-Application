from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by('-time')
    context = {
        "todo_items":todo_items
    }
    return render(request, 'index.html', context)

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    title = request.POST['title']
    desc = request.POST['desc']
    created_obj = Todo.objects.create(time=current_date, text=title, description=desc)
    length_of_todos = Todo.objects.all().count()
    print(length_of_todos)

    return render(request, 'index.html')


