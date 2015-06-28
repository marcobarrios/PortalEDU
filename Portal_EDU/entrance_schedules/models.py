from django.db import models

class EntranceSchedule(models.Model):
    id_entrance_schedule = models.BigIntegerField(primary_key=True, editable=False)
    entrance_time = models.DateTimeField()
    leave_time = models.DateTimeField(blank=True, null=True)
    enable_entrance_schedule = models.BooleanField(default=1)

    staff = models.ForeignKey('staffs.Staff')