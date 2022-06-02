from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            'form':form
        }
        return render(request, 'register.html', context)
    else:
        form = UserCreationForm(request.POST)
        context = {
            "form":form
        }
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('home')
        else:
            return render(request, 'register.html', context)

# def register(request):
#     form = UserCreationForm()
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             form = UserCreationForm()
#
#     context = {
#         'form':form
#     }
#     return render(request, 'register.html', context)


