from django.db import models

class StudentContact(models.Model):
	contact_student = models.CharField(max_length=45)
	contact_extension_student = models.CharField(max_length=10, blank=True, null=True)
	enable_student_contact = models.BooleanField(default=1)

	student = models.ForeignKey('students.Student')

	def __unicode__(self):
		return self.contact_student + " ext " + self.contact_extension_student

