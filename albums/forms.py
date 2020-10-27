from django import forms
from .models import Album, Artist



class AlbumForm(forms.Form):
    title = forms.CharField(max_length=100)
    artist = forms.CharField(max_length=100)
    year_made = forms.DateField()
    image_url = forms.URLField()
       

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = [
            'name',
            'artist_facts',
        ]