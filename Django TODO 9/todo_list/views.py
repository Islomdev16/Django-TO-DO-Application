from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login, logout
from .forms import TODOForm

# Create your views here.
def home(request):
    form = TODOForm()
    context = {
        'form':form
    }
    return render(request, 'index.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username} !')
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = {
        'form':form
    }
    return render(request, 'register.html', context)


