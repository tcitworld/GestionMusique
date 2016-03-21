from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from core.models import *

# Create your views here.
def home(request):
	songs = Song.objects.all().order_by('?')[:20]
	return render(request, 'player/player.html', locals())

def song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'player/song.html', locals())

def author(request, author_id):
	author = get_object_or_404(Author, id=author_id)
	songs = Song.objects.filter(Q(author=author.id) | Q(singer=author.id))
	return render(request, 'player/author.html', locals())