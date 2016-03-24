from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import *
from .forms.userForm import LoginForm


# Create your views here.
def home(request):
	songs = Song.objects.all().order_by('?')[:20]
	form = LoginForm()
	return render(request, 'player/player.html', {'songs':songs,'form':form})

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
    form = LoginForm(request.POST)
    user = authenticate(username=username, password=password)
    if form.is_valid():
        user = authenticate(username=form.cleaned_data.username, password=form.cleaned_data.password)
        if user.is_active:
            login(request, user)
    return home(request)

def register(request):
	return home(request)