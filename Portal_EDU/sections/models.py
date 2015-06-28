from django.db import models

class Section(models.Model):
    id_section = models.BigIntegerField(primary_key=True, editable=False)
    name_section = models.CharField(max_length=10)
    enable_section = models.BooleanField(default=1)