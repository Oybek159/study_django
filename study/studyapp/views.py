from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# rooms = [
#     {'id': 1, 'name': 'Learn Python'},
#     {'id': 2, 'name': 'Frontend Developer'},
#     {'id': 3, 'name': 'Design with me'}
# ]


def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'studyapp/login_register.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

    

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q) |
                                Q(name__icontains=q) |
                                Q(descrioption__icontains=q) |
                                Q(host__username__icontains=q))
    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'studyapp/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'studyapp/room.html', context)

def createroom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'studyapp/room_form.html', context)

def updateroom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'studyapp/room_form.html', context)

def deleteroom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'studyapp/delete.html', {'obj': room})