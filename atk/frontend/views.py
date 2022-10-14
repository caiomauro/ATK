from django.shortcuts import render

# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'frontend/home.html')

def login(request, *args, **kwargs):
    return render(request, 'frontend/login.html')

def auth(request, *args, **kwargs):
    return render(request, 'frontend/auth.html')