from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task_create/', TaskCreate.as_view(), name='create_task'),
    path('task_update/<int:pk>/', TaskUpdate.as_view(), name='update_task'),
    path('task_delete/<int:pk>/', TaskDelete.as_view(), name='delete_task'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
]