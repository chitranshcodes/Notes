from django.shortcuts import render, redirect
from .models import Notes
from .forms import RegisterForm, LoginForm, NoteForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

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

@login_required
def add_note(request):
    if request.method=='POST':
        form=NoteForm(request.POST)
        current_user=request.user
        if form.is_valid():
            title=form.cleaned_data['title']
            content=form.cleaned_data['content']
            Notes.objects.create(title=title, content=content, user=current_user)
            messages.success(request, 'Note created!')
            return redirect('notes:home')
    else:
        form=NoteForm()
    return render(request, 'add_note.html', {'form':form})


@login_required
def update(request, note_id):
    note=Notes.objects.filter(id=note_id).first()
    if request.method=='POST':
        form=NoteForm(request.POST)
        if form.is_valid():
            note.title=form.cleaned_data['title']
            note.content=form.cleaned_data['content']
            note.date=timezone.now()
            note.save()
            messages.success(request, f'updated the note! {note.title}')
            return redirect('notes:home')
    else:
        form=NoteForm(initial={'title':note.title, 'content':note.content})

    return render(request, 'update.html', {'form':form, 'note':note})

@login_required
def logout(request):
    logout(request)
    return redirect('notes:login')