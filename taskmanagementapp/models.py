from django.db import models
from user.models import CustomUser
# Create your models here.


class Tasks(models.Model):
    
    STATUS_CHOICES = {
        
        ('pending', 'Pending'),
        ('in_progress', 'In  Progress'),
        ('completed', 'Completed')
    }
    
    PRIORITY_CHOICES = {
        ('low','LOW'),
        ('medium', 'MEDIUM'),
        ('high', 'HIGH')
    }
    
    
    task_title = models.CharField(max_length=300) 
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='created_tasks')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')  # Optional assignee
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='low')
    due_date = models.DateTimeField(null=True, blank=True)  # Optional due date for the task
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set to the current time when created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update to the current time when modified
    
    def __str__(self):
        return self.task_title
    
    class Meta:
        ordering = ['-created_at']




