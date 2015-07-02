# -*- encoding: utf-8 -*-
from django.db import models

class Grade(models.Model):
	max_grade_capacity = models.PositiveIntegerField(blank=True, null=True)
	quantity_student_grade = models.PositiveIntegerField(blank=True, null=True)
	enable_grade = models.BooleanField(default=1)

	grade_name = models.ForeignKey('grade_names.GradeName')
	section = models.ForeignKey('sections.Section')
	staff = models.ForeignKey('staffs.Staff', blank=True, null=True)
	level = models.ForeignKey('levels.Level')

	def __str__(self):
		return str(self.grade_name) + " " + str(self.level) + " " + str(self.section)