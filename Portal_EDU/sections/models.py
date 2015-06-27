from django.db import models

class Section(models.Model):
    id_section = models.BigIntegerField(primary_key=True)
    name_section = models.CharField(max_length=5)
    enable_section = models.BooleanField(default=1)