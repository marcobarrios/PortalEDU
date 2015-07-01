from django.db import models

class Course(models.Model):
	max_student_capacity_course = models.PositiveIntegerField(blank=True, null=True)
	quantity_student_course = models.PositiveIntegerField(blank=True, null=True)
	enable_course = models.BooleanField(default=1)

	grade = models.ForeignKey('grades.Grade')
	subject = models.ForeignKey('subjects.Subject')
	module = models.ForeignKey('modules.Module')
	planifications = models.ManyToManyField('planifications.Planification', blank=True, null=True)
	schedule = models.ForeignKey('schedules.Schedule', blank=True, null=True)
	classroom = models.ForeignKey('classrooms.ClassRoom', blank=True, null=True)