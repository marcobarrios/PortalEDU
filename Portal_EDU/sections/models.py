from django.db import models

class Section(models.Model):
    name_section = models.CharField(max_length=10)
    enable_section = models.BooleanField(default=1)

    def __unicode__(self):
    	return self.name_section