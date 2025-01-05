from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'amir'},
    {'id': 2, 'name': 'abdolboriy'},
    {'id': 3, 'name': 'nazar'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html')