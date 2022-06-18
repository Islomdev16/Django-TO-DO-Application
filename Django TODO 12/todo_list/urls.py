from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]