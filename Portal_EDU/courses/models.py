from django.db import models

class Course(models.Model):
	id_course = models.BigIntegerField(primary_key=True)
	max_student_capacity_course = models.PositiveIntegerField(blank=True, null=True)
	quantity_student_course = models.PositiveIntegerField(blank=True, null=True)
	enable_course = models.BooleanField(default=1)