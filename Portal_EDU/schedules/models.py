from django.db import models

class Schedule(models.Model):
    init_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    enable_schedule = models.BooleanField(default=1)