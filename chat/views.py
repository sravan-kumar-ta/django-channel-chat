from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def test(request):
    return render(request, 'chat.html')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')
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


def enter_room(request, user1_id, user2_id):
    if user1_id > user2_id:
        user1_id, user2_id = user2_id, user1_id
    user1 = User.objects.get(id=user1_id)
    user2 = User.objects.get(id=user2_id)
    room_name = str(user1.username + '_chat_with_' + user2.username)
#     return redirect('home')
#
#
# def room(request, room_name):
    return render(request, 'chatroom.html', {'room_name': room_name})
