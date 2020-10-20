from django.db import models



class Album(models.Model):
  
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    year_made = models.DateField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)
   

    def __str__(self):
        return self.title