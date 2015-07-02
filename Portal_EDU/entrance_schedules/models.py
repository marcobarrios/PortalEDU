# -*- encoding: utf-8 -*-
from django.db import models

class EntranceSchedule(models.Model):
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
	entrance_time = models.TimeField()
	leave_time = models.TimeField(blank=True, null=True)
	enable_entrance_schedule = models.BooleanField(default=1)

	staff = models.ForeignKey('staffs.Staff')

	def __str__(self):
		return str(self.day) + " " + str(self.entrance_time) + " - " + str(self.leave_time)