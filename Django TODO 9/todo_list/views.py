from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

# def register(request):
#     if request.method == 'GET':
#         form = UserCreationForm()
#         context = {
#             'form':form
#         }
#         return render(request, 'register.html', context)
#     else:
#         form = UserCreationForm(request.POST)
#         context = {
#             "form":form
#         }
#         if form.is_valid():
#             user = form.save()
#             if user is not None:
#                 return redirect('home')
#         else:
#             return render(request, 'register.html', context)

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


