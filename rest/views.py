from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import CustomUser
from rest.serializers import UserSerializer
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
