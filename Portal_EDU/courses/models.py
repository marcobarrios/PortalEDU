from django.db import models

class Course(models.Model):
	id_course = models.BigIntegerField(primary_key=True)
	max_student_capacity_course = models.IntegerField()
	quantity_student_course = models.IntegerField()
	enable_course = BooleanField(default=1)