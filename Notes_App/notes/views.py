from django.shortcuts import render, redirect
from .models import Notes
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    notes=Notes.objects.all()
    return render(request, 'home.html', {'notes':notes})

def Login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user= authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Logged In Successfully!")
                return redirect('notes:home')
            else:
                if User.objects.filter(username=username).exists():
                    form.add_error('password', 'Wrong Password')
                else:
                    form.add_error('username', "user doesn't exist.")

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

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
                messages.success(request, "Registered Successfully🤩 Login now!")
                return redirect('notes:login')
    else:
        form=RegisterForm()

    return render(request, 'register.html', {'form':form})

def about(request):
    return render(request, 'about.html')
