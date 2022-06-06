from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import logout
from .forms import TODOForm
from django.contrib.auth.decorators import login_required
from .models import TODO

# Create your views here.
@login_required(login_url='loginUser')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user=user).order_by('-date')
        context = {
            'form': form,
            'todos': todos
        }
        return render(request, 'index.html', context)

# @login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')
        else:
            return render(request, 'index.html', {'form': form})


def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})


def registerUser(request):
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


def logoutUser(request):
    logout(request)
    return redirect('login')

def deleteTask(request, pk):
    TODO.objects.get(id=pk).delete()
    return redirect('home')