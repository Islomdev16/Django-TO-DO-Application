from django.urls import path
from . import views

urlpatterns = [
    path('get_todos/', views.getTodos, name='get_todos'),
    path('get_todo/<int:pk>/', views.getTodo, name='get_todo'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('update_todo/<int:pk>/', views.update_todo, name='update_todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
]

# http://127.0.0.1:8000/api/get_todos/
# http://127.0.0.1:8000/api/get_todo/id/
# http://127.0.0.1:8000/api/create_todo/
# http://127.0.0.1:8000/api/update_todo/id/
# http://127.0.0.1:8000/api/delete_todo/id/