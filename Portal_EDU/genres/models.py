from django.db import models

class Genre(models.Model):
    genre = models.CharField(max_length=20)
    enable_genre = models.BooleanField(default=1)

    def __unicode__(self):
    	return self.genre