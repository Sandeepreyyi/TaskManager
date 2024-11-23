from django.contrib import admin
from .models import *
# Register your models here.


class CustomUserDisplay(admin.ModelAdmin):
    list_display = ['id','email','first_name','last_name','is_active']
    exclude = ('groups', 'user_permissions')


admin.site.register(CustomUser,CustomUserDisplay)