from django.db import models

class StudentControlList(models.Model):
	year = models.PositiveIntegerField(blank=True)
	gpa = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
	approved = models.BooleanField(default=0)
	enable_student_control_list = models.BooleanField(default=1)

	student = models.ForeignKey('students.Student')
	grade = models.ForeignKey('grades.Grade')