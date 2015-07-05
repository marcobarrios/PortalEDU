# -*- encoding: utf-8 -*-
from django.db import models

class StaffEntranceSchedule(models.Model):
	enable_staff_entrance_schedule = models.BooleanField(default=True)

	staff = models.ForeignKey('staffs.Staff')
	entrance_schedule = models.ManyToManyField('entrance_schedules.EntranceSchedule')

	def __str__(self):
		return "Horarios de Entrada de: " + str(self.staff)