from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from core.models import *

# Create your views here.
def home(request):
    return render(request, 'player/player.html', locals())

def song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'player/song.html', locals())
