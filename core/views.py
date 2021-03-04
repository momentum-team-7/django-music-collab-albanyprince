from django.shortcuts import render, get_object_or_404
from .models import Album, Artist
from .forms import AlbumForm, ArtistForm
from django.http import HttpResponseRedirect
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

def add_artist(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ArtistForm()

    return render(request, 'core/add_artist.html', {'form': form})

def add_album(request):
   
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AlbumForm()

    return render(request, 'core/add_album.html', {'form': form})

def edit_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'POST':    
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ArtistForm(instance=artist)        
    return render(request, 'core/edit_artist.html',{'form': form, 'artist': artist})    

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':    
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/album')
    else:
        form = AlbumForm(instance=album)        
    return render(request, 'core/edit_album.html',{'form': form, 'album': album})      

def delete_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)   
    artist.delete()
    return HttpResponseRedirect('/')