# -*- encoding: utf-8 -*-
from django.db import models

class StaffEntranceReport(models.Model):
    date_time_staff_entrance = models.DateTimeField(auto_now_add=True)
    date_time_staff_exit = models.DateTimeField(auto_now=True, blank=True, null=True)
    enable_staff_entrance_report = models.BooleanField(default=1)

    staff = models.ForeignKey('staffs.Staff')

    def __str__(self):
    	return str(self.date_time_staff_entrance) + " - " + str(self.date_time_staff_exit)