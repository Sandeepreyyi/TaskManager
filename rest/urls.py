from django.urls import path
from rest.views import *


urlpatterns = [
    path('users/',CustomUserList.as_view(), name='user-list'),
    
    path('tasks/',TaskList.as_view(), name='task-list'),
    
]
