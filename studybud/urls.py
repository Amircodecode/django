from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse('hello world')

def room(request):
    return HttpResponse('room')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('room/', room)
]

