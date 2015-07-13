from django.db import models

class StaffContact(models.Model):
	contact_staff = models.CharField(max_length=45)
	contact_extension_staff = models.CharField(max_length=10, blank=True, null=True)
	enable_staff_contact = models.BooleanField(default=1)

	contact_type = models.ForeignKey('contact_types.ContactType')
	staff = models.ForeignKey('staffs.Staff')

	def __unicode__(self):
		return self.contact_staff + " ext " + self.contact_extension_staff
