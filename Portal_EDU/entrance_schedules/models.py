from django.db import models

class EntranceSchedule(models.Model):
    entrance_time = models.DateTimeField()
    leave_time = models.DateTimeField(blank=True, null=True)
    enable_entrance_schedule = models.BooleanField(default=1)

    staff = models.ForeignKey('staffs.Staff')