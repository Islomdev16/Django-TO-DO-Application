from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('login/', views.loginUser, name='loginUser'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('delete/<int:pk>/', views.deleteTask, name='delete'),
    path('change_status/<int:pk>/<str:status>', views.change_status, name='change_status')
]
