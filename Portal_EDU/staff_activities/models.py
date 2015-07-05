# -*- encoding: utf-8 -*-
from django.db import models

class StaffActivity(models.Model):
    name_staff_activity = models.CharField(max_length=45)
    date_time_staff_activity = models.DateTimeField(blank=True, null=True)
    descripcion_staff_activity = models.TextField(blank=True)
    done_staff_activity = models.BooleanField(default=False)
    enable_staff_activity = models.BooleanField(default=1)

    staff = models.ManyToManyField('staffs.Staff')

    def __str__(self):
    	return self.name_staff_activity + " " + str(self.date_time_staff_activity)