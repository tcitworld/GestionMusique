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
    return render(request, 'player/album.html', locals())

def artist(request, artist_id):
	artist = get_object_or_404(Artist, id=artist_id)
	albums = Album.objects.filter(artist=artist.id)
	return render(request, 'player/artist.html', locals())

def group(request, group_id):
	group = get_object_or_404(Group, id=group_id)
	albums = Album.objects.filter(group=group.id)
	return render(request, 'player/group.html', locals())

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