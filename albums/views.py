from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Album, Artist
from .forms import AlbumForm

# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html",
                  {"albums": albums})

def add_albums(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            title = data.get("title")
            artist = data.get("artist")
            year_made = data.get("year_made")
            image_url = data.get("image_url")
            artist = Artist.objects.get_or_create(name=artist)[0]
            album = Album.objects.create(title=title, artist=artist, year_made=year_made, image_url=image_url)
            return redirect(to='list_albums')

    return render(request, "albums/add_albums.html", {"form": form})

def edit_albums(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/edit_albums.html", {
        "form": form,
        "album": album,
    })

def delete_albums(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, "albums/delete_albums.html",
                  {"album": album})
    
def detail_albums(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.artist()
        return redirect(to='list_albums')

    return render(request, "albums/detail_albums.html",
                  {"album": album})