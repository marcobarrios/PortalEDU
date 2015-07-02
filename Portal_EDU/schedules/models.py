# -*- encoding: utf-8 -*-
from django.db import models

class Schedule(models.Model):
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
	init_time = models.TimeField()
	end_time = models.TimeField()
	enable_schedule = models.BooleanField(default=1)

	def __unicode__(self):
		return str(self.day) + " " + str(self.init_time) + " - " + str(self.end_time)