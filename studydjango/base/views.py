from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
rooms = [
    {'id' : 1, 'name' : 'Python'},
    {'id' : 2, 'name' : 'SQL'},
    {'id' : 3, 'name' : 'Front End'},
]

def home(request):
    return render(request, 'base/home.html', {'rooms' : rooms})

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    
    context = {'room': room}
    return render(request, 'base/room.html', context)
