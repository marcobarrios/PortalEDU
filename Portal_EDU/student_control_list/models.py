from django.db import models

class StudentControlList(models.Model):
	year = models.PositiveIntegerField()
	gpa = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
	approved = models.BooleanField(default=0)
	enable_student_control_list = models.BooleanField(default=1)

	student = models.ForeignKey('students.Student')
	grade = models.ForeignKey('grades.Grade')

	def __str__(self):
		return self.year + " " + self.student + " " + self.grade + " " + self.gpa