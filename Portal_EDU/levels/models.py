from django.db import models

class Level(models.Model):
    id_level = models.BigIntegerField(primary_key=True)
    level_name = models.CharField(max_length=45)
    enable_levels = models.BooleanField(default=1)