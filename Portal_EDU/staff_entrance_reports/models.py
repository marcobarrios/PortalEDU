from django.db import models

class StaffEntranceReport(models.Model):
    id_staff_entrance_report = models.BigIntegerField(primary_key=True)
    date_time_staff_entrance = models.DateTimeField()
    date_time_staff_exit = models.DateTimeField(blank=True, null=True)
    enable_staff_entrance_report = models.BooleanField(default=1)