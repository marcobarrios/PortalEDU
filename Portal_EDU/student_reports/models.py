# -*- encoding: utf-8 -*-
from django.db import models

class StudentReport(models.Model):
    subject_student_report = models.CharField(max_length=45)
    description_student_report = models.TextField(blank=True) 
    date_time_sent_report = models.DateTimeField(auto_now_add=True)
    checked_report = models.BooleanField(default=False)
    date_time_checked_report = models.DateTimeField(blank=True, null=True)
    enable_student_report = models.BooleanField(default=1)

    student = models.ForeignKey('students.Student')

    def __str__(self):
    	return self.subject_student_report