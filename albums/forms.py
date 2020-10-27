from django import forms
from .models import Album, Artist



class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',
            'year_made',
            'image_url',
        ]

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = [
            'name',
            'artist_facts',
        ]