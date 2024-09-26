from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import UserAccount
from .forms import CustomUserCreationForm

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = UserAccount.objects.create_user(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Trying to authenticate: {email}")
        try:
            user = UserAccount.objects.get(email=email)
        except UserAccount.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            print(f"Email entered: {email}, Password entered: {password}")
            print("Authentication failed")
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def main_page(request):
    tasks = Task.objects.all()
    return render(request, 'main_page.html', {'tasks': tasks})

