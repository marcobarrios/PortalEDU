from django.db import models

class Course(models.Model):
	id_course = models.BigIntegerField(primary_key=True)
	max_student_capacity_course = models.PositiveIntegerField(blank=True, null=True)
	quantity_student_course = models.PositiveIntegerField(blank=True, null=True)
	enable_course = models.BooleanField(default=1)

	grade = models.ForeignKey('grades.Grade')
	subject = models.ForeignKey('subjects.Subject')
	schedule = models.ForeignKey('schedules.Schedule')
	planification = models.ForeignKey('planifications.Planification')
	module = models.ForeignKey('modules.Module')
	classroom = models.ForeignKey('classrooms.ClassRoom')