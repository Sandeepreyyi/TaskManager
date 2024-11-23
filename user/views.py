from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from user.forms import UserRegistrationForm

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            # Save user instance without committing to set the password
            user = form.save(commit=False)
            user.set_password('defaultpassword')  # Set a default or generated password
            user.save()
            
            # Return a JSON response with a success message
            return JsonResponse({'message': 'User registered successfully!'}, status=200)
        else:
            # If form is invalid, return an error message in JSON format
            return JsonResponse({'message': 'There were errors in the form.'}, status=400)
    
    # If not POST, return a message saying form submission is expected
    return JsonResponse({'message': 'Please submit the form via POST request.'}, status=400)
