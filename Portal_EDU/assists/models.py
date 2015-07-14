from django.db import models

class Assistance(models.Model):
	title_assistance = models.CharField(max_length=45, blank=True, null=True)
	date_assistance = models.DateField()

	course = models.ForeignKey('courses.Course')
	students = models.ManyToManyField('students.Student')

	def __unicode__(self):
		return self.title_assistance + " " + str(self.date_assistance) + " " + str(self.course)

