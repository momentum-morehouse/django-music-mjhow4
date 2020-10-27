from django.db import models



class Album(models.Model):
  
    title = models.CharField(max_length=255)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE, related_name="albums", null=True, blank=True)
    year_made = models.DateField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)
   

    def __str__(self):
        return self.title

class Artist(models.Model):

    name = models.CharField(max_length=100)
    artist_facts = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name