from django.db import models

class StaffAppointment(models.Model):
    id_staff_appointment = models.BigIntegerField(primary_key=True)
    subject_staff_appointment = models.CharField(max_length=45, blank=True)
    description_staff_appointment = models.CharField(max_length=45, blank=True) 
    date_time_staff_appointment = models.DateTimeField(blank=True, null=True)
    duration_staff_appointment = models.PositiveIntegerField(blank=True, null=True)
    confirmation_staff_appointment = models.BooleanField(default=0)
    status_staff_appointment = models.BooleanField(default=1)
    enable_staff_appointment = models.BooleanField(default=1) 