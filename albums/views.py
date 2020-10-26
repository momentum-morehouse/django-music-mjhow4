from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Album
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
            form.save()
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
    albums = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        albums.delete()
        return redirect(to='list_albums')

    return render(request, "albums/delete_albums.html",
                  {"albums": albums})