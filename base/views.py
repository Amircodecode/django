from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'amir'},
    {'id': 2, 'name': 'abdolboriy'},
    {'id': 3, 'name': 'nazar'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
        context = {'room': room}
    return render(request, 'base/room.html', context)