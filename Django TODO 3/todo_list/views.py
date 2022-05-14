from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def home(request):
    context = {"success": False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Task(title=title, description=desc)
        ins.save()
        context = {
            "success": True,
            "title":title
        }

    return render(request, 'index.html', context)

def tasks(request):
    return render(request, 'tasks.html')
