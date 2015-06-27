from django.db import models

class StudentControlList(models.Model):
	id_student_control_list = models.BigIntegerField(primary_key=True)
	approved_student = models.BooleanField(default=0)
	enable_student_control_list = models.BooleanField(default=1)