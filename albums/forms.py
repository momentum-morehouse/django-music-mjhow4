from django import forms
from .models import Album



class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',
            'year_made',
            'image_url',
        ]