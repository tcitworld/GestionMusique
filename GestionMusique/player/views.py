from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import *
from .forms.userForm import *


# Create your views here.
def home(request,message=""):
	songs = Song.objects.all().order_by('?')[:20]
	form = LoginForm()
	return render(request, 'player/player.html', {'songs':songs,'form':form,'message':message})


def song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'player/song.html', locals())

def artist(request, artist_id):
	artist = get_object_or_404(Artist, id=artist_id)
	songs = Song.objects.filter(artist=artist.id)
	return render(request, 'player/artist.html', locals())

def group(request, group_id):
	group = get_object_or_404(Group, id=group_id)
	songs = Song.objects.filter(group=group.id)
	return render(request, 'player/group.html', locals())

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    message = 'Username or password invalid'
    if user is not None:
        if user.is_active:
            login(request, user)
            message = "Hi, have a good moment"
    return home(request,message)

def register(request):
	register = RegisterForm()
	return render(request,'player/register.html', locals())

def logout(request):
	return home(request)