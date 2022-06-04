from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'index.html')



# def loginUser(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             messages.success(request, f'Login is done successfully for {username} !')
#             return redirect('home')
#         else:
#             return redirect('login')
#             # messages.success(request, '❌ Username or password is incorrect')


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


