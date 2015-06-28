from django.db import models

class StaffEntranceReport(models.Model):
    date_time_staff_entrance = models.DateTimeField()
    date_time_staff_exit = models.DateTimeField(blank=True, null=True)
    enable_staff_entrance_report = models.BooleanField(default=1)

    staff = models.ForeignKey('staffs.Staff')