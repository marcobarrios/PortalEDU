from django.db import models

class Note(models.Model):
	note = models.DecimalField(default=0.0, max_digits=4, decimal_places=2)
	enable_note = models.BooleanField(default=1)

	academic_calendar = models.ForeignKey('academic_calendars.AcademicCalendar')
	student = models.ForeignKey('students.Student')

	def __str__(self):
		return self.note
