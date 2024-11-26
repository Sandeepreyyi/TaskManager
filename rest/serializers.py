from rest_framework import serializers
from user.models import *
from taskmanagementapp.models import *

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = '__all__'
        


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tasks
        
        fields = '__all__'