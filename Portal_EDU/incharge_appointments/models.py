from django.db import models

class InchargeAppointment(models.Model):
    id_incharge_appointment = models.BigIntegerField(primary_key=True)
    subject_incharge_appointment = models.CharField(max_length=45, blank=True)
    description_incharge_appointment = models.TextField(blank=True)
    date_time_incharge_appointment = models.DateTimeField(blank=True, null=True)
    duration_incharge_appointment = models.IntegerField(blank=True, null=True)
    confirmation_incharge_appointment = models.BooleanField(default=0)
    status_incharge_appointment = models.BooleanField(default=1)
    enable_incharge_appointment = models.BooleanField(default=1)