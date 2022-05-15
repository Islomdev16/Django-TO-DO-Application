from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks, name="tasks"),
    path("update_task/<str:pk>/", views.updateTask, name='update_task'),
    path("delete_task/<int:pk>/", views.deleteTask, name='delete_task'),
]