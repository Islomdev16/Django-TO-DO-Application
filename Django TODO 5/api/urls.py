from django.urls import path
from . import views

urlpatterns = [
    path('', views.getTodos, name='get_todos'),
    path('<int:pk>/', views.getTodo, name='get_todo'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('update_todo/<int:pk>/', views.update_todo, name='update_todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
]