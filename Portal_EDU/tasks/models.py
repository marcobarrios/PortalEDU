# -*- encoding: utf-8 -*-
from django.db import models

class Task(models.Model):
	title_task = models.CharField(max_length=45, blank=True, null=True)
	text_task = models.TextField(blank=True, null=True)
	delivered_date_task = models.DateTimeField(auto_now=True)
	checked_task = models.BooleanField(default=False)
	file_task = models.FileField(upload_to='task_files/%Y/%m/%d/', blank=True)
	teacher_commentary_task = models.TextField(blank=True) 
	enable_task = models.BooleanField(default=1) 

	student = models.ForeignKey('students.Student')
	academic_calendar = models.ForeignKey('academic_calendars.AcademicCalendar')

	def __str__(self):
		return str(self.student) + " - " + str(self.academic_calendar) + " - " + str(self.delivered_date_task)