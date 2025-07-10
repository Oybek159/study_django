from django.shortcuts import render
from .models import Room

# rooms = [
#     {'id': 1, 'name': 'Learn Python'},
#     {'id': 2, 'name': 'Frontend Developer'},
#     {'id': 3, 'name': 'Design with me'}
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'studyapp/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'studyapp/room.html', context)

def createroom(request):
    context = {}
    return render(request, 'studyapp/room_form.html', context)
