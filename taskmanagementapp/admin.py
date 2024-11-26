from django.contrib import admin
from taskmanagementapp.models import *
# Register your models here.


class TasksDisplay(admin.ModelAdmin):
    list_display = ['id','task_title','created_by','assigned_to','status','created_at','updated_at']
    
    list_filter = ['status']
    # exclude = ('groups', 'user_permissions')




admin.site.register(Tasks,TasksDisplay)
