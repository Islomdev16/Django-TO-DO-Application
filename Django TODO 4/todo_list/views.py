from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by('-added_time')
    context = {
        "todo_items":todo_items
    }
    return render(request, 'index.html', context)

@csrf_exempt
def add_todo(request):
    if not request.POST['title'] == '':
        current_date = timezone.now()
        title = request.POST['title']
        new_task = Todo.objects.create(added_time=current_date, title=title)
        length_of_todos = Todo.objects.all().count()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

@csrf_exempt
def task_delete(request, pk):
    Todo.objects.get(id=pk).delete()
    return HttpResponseRedirect('/')

