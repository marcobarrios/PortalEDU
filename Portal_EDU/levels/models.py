from django.db import models

class Level(models.Model):
    level_name = models.CharField(max_length=45)
    enable_levels = models.BooleanField(default=1)

    def __unicode__(self):
    	return self.level_name