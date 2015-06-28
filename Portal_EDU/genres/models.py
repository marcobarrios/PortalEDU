from django.db import models

class Genre(models.Model):
    id_genre = models.BigIntegerField(primary_key=True, editable=False)
    genre = models.CharField(max_length=20)
    enable_genre = models.BooleanField(default=1)