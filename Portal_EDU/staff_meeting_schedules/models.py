# -*- encoding: utf-8 -*-
from django.db import models

class StaffMeetingSchedule(models.Model):
	week_days = (
		('Lunes', 'Lunes'),
		('Martes', 'Martes'),
		('Miércoles', 'Miércoles'),
		('Jueves', 'Jueves'),
		('Viernes', 'Viernes'),
		('Sábado', 'Sábado'),
		('Domingo', 'Domingo'),
	)
	day = models.CharField(max_length=15, choices=week_days, default='Lunes')
	date_time_init_staff_meeting_schedule = models.TimeField()
	date_time_end_staff_meeting_schedule = models.TimeField()
	enable_staff_meeting_schedule = models.BooleanField(default=1)

	staff = models.ForeignKey('staffs.Staff')

	def __str__(self):
		return str(self.day) + " - " + str(self.date_time_init_staff_meeting_schedule) + " - " + str(self.date_time_end_staff_meeting_schedule)
