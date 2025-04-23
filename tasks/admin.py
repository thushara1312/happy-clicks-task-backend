from django.contrib import admin

from .models import Task


@admin.register(Task)   
class TaskAdmin(admin.ModelAdmin):  
    list_display = ('title', 'description', 'due_date', 'priority', 'status')