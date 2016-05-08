from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from .forms.userForm import *


# Create your views here.
def home(request,message=""):
	albums = Album.objects.all().order_by('?')[:20]
	form = LoginForm()
	return render(request, 'player/player.html', {'albums':albums,'form':form,'message':message})


def album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    playlists = Playlist.objects.all()
    return render(request, 'player/album.html', locals())

def artist(request, artist_id):
	artist = get_object_or_404(Artist, id=artist_id)
	albums = Album.objects.filter(artist=artist.id)
	return render(request, 'player/artist.html', locals())

def group(request, group_id):
	group = get_object_or_404(Group, id=group_id)
	albums = Album.objects.filter(group=group.id)
	return render(request, 'player/group.html', locals())

def genre(request, genre_id):
	genre = get_object_or_404(Genre, id=genre_id)
	albums = Album.objects.filter(genres=genre.id)
	return render(request, 'player/genres.html', locals())

def loginUser(request):
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
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'],email=form.cleaned_data['email'],password=form.cleaned_data['password'],first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'])
			return loginUser(request)
	register = RegisterForm()
	form = LoginForm()
	return render(request,'player/register.html', locals())

def logoutUser(request):
	logout(request)
	return home(request)

def search(request):
    search = request.POST['search'] if request.POST['search'] else ""
    albums = Album.objects.filter(title__contains=str(search))
    artists = Artist.objects.filter(name__contains=str(search))
    genres = Genre.objects.filter(label__contains=str(search))
    return render(request, 'player/search.html', locals())

def playlists(request):
	playlists = Playlist.objects.all()
	return render(request, 'player/playlists.html', locals())

def playlist(request, playlist_id):
	playlist = get_object_or_404(Playlist, id=playlist_id)
	songs = Selection.objects.filter(playlist=playlist.id)
	return render(request, 'player/playlist.html', locals())

def addplaylist(request):
	name = request.POST['playlistName'] if request.POST['playlistName'] else ""
	user = request.user
	playlist = Playlist(title=name, user=user)
	playlist.save()
	return render(request, 'player/playlists.html')

def addsongtoplaylist(request, song_id):
	song = Song.objects.get_or_create(id=song_id)
	playlist.songs.add(song)

def deleteplaylist(request, playlist_id):
	playlist = get_object_or_404(Playlist, id=playlist_id)
	playlist.delete()
	return render(request, 'player/playlists.html')