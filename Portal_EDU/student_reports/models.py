from django.db import models

class StudentReport(models.Model):
    id_student_report = models.BigIntegerField(primary_key=True)
    subject_student_report = models.CharField(max_length=45, blank=True)
    description_student_report = models.TextField(blank=True) 
    date_time_sent_report = models.DateTimeField(blank=True, null=True)
    checked_report = models.BooleanField(default=0)
    date_time_checked_report = models.DateTimeField(blank=True, null=True)
    enable_student_report = models.BooleanField(default=1)

    student = models.ForeignKey('students.Student')