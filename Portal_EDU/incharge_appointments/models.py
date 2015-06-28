from django.db import models

class InchargeAppointment(models.Model):
    subject_incharge_appointment = models.CharField(max_length=45, blank=True)
    description_incharge_appointment = models.TextField(blank=True)
    date_time_incharge_appointment = models.DateTimeField(blank=True, null=True)
    duration_incharge_appointment = models.PositiveIntegerField(blank=True, null=True)
    confirmation_incharge_appointment = models.BooleanField(default=0)
    status_incharge_appointment = models.BooleanField(default=1)
    enable_incharge_appointment = models.BooleanField(default=1)

    staff = models.ForeignKey('staffs.Staff')
    student = models.ForeignKey('students.Student')

    def __unicode__(self):
        return self.subject_incharge_appointment