from django.db import models

class Schedule(models.Model):
    id_schedule = models.BigIntegerField(primary_key=True)
    init_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    enable_schedule = models.BooleanField(default=1)