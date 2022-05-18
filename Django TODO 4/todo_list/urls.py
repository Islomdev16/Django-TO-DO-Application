from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_todo/', views.add_todo, name="add_todo"),
    path('task_delete/<int:pk>/', views.task_delete, name='task_delete')
]
