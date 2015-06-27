from django.db import models

class Planification(models.Model):
    id_planification = models.BigIntegerField(primary_key=True)
    planification_file = models.FileField(blank=True)
    description_planification = models.TextField(blank=True, null=True)
    enable_planification = models.BooleanField(default=1)