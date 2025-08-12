from django.shortcuts import render, redirect
from .models import Notes
from .forms import RegisterForm
from django.contrib.auth.models import User


def home(request):
    notes=Notes.objects.all()
    return render(request, 'home.html', {'notes':notes})

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already taken')
            elif User.objects.filter(email=email).exists():
                form.add_error('email', 'Email already registered')
            else:
                User.objects.create_user(username=username,email=email,password=password)
            
                return redirect('notes:login')
    else:
        form=RegisterForm()

    return render(request, 'register.html', {'form':form})

def about(request):
    return render(request, 'about.html')
