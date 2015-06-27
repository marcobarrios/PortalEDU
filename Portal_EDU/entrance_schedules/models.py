from django.db import models

class EntranceSchedule(models.Model):
    id_entrance_schedule = models.BigIntegerField(primary_key=True)
    entrance_time = models.TimeField()
    leave_time = models.TimeField(blank=True, null=True)
    enable_entrance_schedule = models.BooleanField(default=1)