from .models import Room

for room in Room.objects.all():
    print(room)