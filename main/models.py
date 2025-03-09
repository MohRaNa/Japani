from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserLibrary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario que agrega el anime
    mal_id = models.IntegerField()  # ID del anime en MyAnimeList
    title = models.CharField(max_length=255)  # Título del anime
    image_url = models.URLField()  # URL de la imagen del anime
    synopsis = models.TextField()  # Sinopsis del anime
    url = models.URLField()  # URL del anime en MyAnimeList

    def __str__(self):
        return f"{self.title} (added by {self.user.username})"