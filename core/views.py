from django.shortcuts import render
from .models import Album, Artist

# Create your views here.
def index(request):
    artists = Artist.objects.all()
    return render(request, 'index.html', {'artists': artists})

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list', {'albums': albums})

def artist_detail(request):
    artist = Artist.objects.all()  
    return render(request, 'artist_detail', {'artist': artist})  