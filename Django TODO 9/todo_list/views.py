from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'register.html', context)
