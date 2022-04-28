from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "complete", "created"]
    list_filter = ["complete"]
