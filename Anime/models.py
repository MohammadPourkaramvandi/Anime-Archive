from django.db import models
from django.urls import reverse

class AnimeItems(models.Model):
    anime_picture = models.ImageField(upload_to='static/picture', blank=True)
    title = models.CharField(max_length=500)
    seasone = models.PositiveIntegerField(blank=True)
    episod = models.PositiveIntegerField(blank=True)
    
    def get_absolute_url(self):
        return reverse("update_url", kwargs={"pk": self.pk})