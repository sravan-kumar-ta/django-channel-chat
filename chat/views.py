from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.create_user(
            username=username,
            first_name='first name',
            last_name='last name',
            password='Pa$$w0rd!'
        )
        user.save()
        return redirect('login')
    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = authenticate(request, username=username, password='Pa$$w0rd!')
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong username')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    users = User.objects.exclude(id=request.user.id).exclude(is_staff=1)
    return render(request, 'home.html', {'users': users})


def room(request, room_name):
    return render(request, 'chatroom.html', {'room_name': room_name})
