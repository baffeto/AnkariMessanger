from django.shortcuts import render
from .models import Room, Message
from django.contrib.auth.decorators import login_required


@login_required
def rooms(request):
    rooms = Room.objects.all()
    
    return render(request, 'rooms/rooms.html', {'rooms': rooms})