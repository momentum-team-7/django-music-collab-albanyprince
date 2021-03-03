from django.shortcuts import render, get_object_or_404
from .models import Album, Artist

# Create your views here.
def index(request):
    artists = Artist.objects.all()
    return render(request, 'core/index.html', {'artists': artists})

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'core/album_list.html', {'albums': albums})

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)  
    return render(request, 'core/artist_detail.html', {'artist': artist})  

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'core/album_detail.html', {'album': album})