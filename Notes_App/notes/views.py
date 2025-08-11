from django.shortcuts import render
from .models import Notes

def home(request):
    notes=Notes.objects.all()
    return render(request, 'home.html', {'notes':notes})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def about(request):
    return render(request, 'about.html')


