from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import CustomUser
from taskmanagementapp.models import Tasks
from rest.serializers import *
# from django.http import HTTPResponce
from django.http import HttpResponse

class CustomUserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the user if data is valid
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return HttpResponse("Bad")


class TaskList(APIView):
    def get(self,request):
        
        tasks = Tasks.objects.all()
        serelizer = TaskSerializer(tasks, many=True)
        
        return Response(serelizer.data)
    
    def post(self, request):
        
        serializer = TaskSerializer(data= request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request,pk):
        
        # serializer = TaskSerializer(data= request.data)
        
        try :
            
            task = Tasks.objects.get(pk=pk)
            
        except Tasks.DoesNotExist:

            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
        serializer = TaskSerializer(task, data= request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
        
        

        
        
        
            
        