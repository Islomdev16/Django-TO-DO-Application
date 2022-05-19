from django.urls import path
from . import views

urlpatterns = [
    path('', views.getTodos, name='get_todos'),
    path('<int:pk>/', views.getTodo, name='get_todo')
]