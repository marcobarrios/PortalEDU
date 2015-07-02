# -*- encoding: utf-8 -*-
from django.db import models

class StaffAppointment(models.Model):
    subject_staff_appointment = models.CharField(max_length=45)
    description_staff_appointment = models.CharField(max_length=45, blank=True) 
    date_time_staff_appointment = models.DateTimeField(blank=True, null=True)
    duration_staff_appointment = models.PositiveIntegerField(blank=True, null=True, help_text="En minutos")
    confirmation_staff_appointment = models.BooleanField(default=False)
    status_staff_appointment = models.BooleanField(default=True)
    enable_staff_appointment = models.BooleanField(default=1) 

    student = models.ForeignKey('students.Student')
    staff = models.ForeignKey('staffs.Staff')

    def __str__(self):
        return self.subject_staff_appointment