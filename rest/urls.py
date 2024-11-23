from django.urls import path
from rest.views import CustomUserList


urlpatterns = [
    path('users/',CustomUserList.as_view(), name='user-list')
]
