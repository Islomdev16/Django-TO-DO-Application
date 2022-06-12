from django.urls import path
from .import views

urlpatterns = [
    path('', views.homeTask, name='home'),
    path('update/<int:pk>/', views.updateTask, name='update'),
]