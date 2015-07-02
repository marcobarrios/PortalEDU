from django.db import models

class Contact(models.Model):
    phone_contact = models.CharField(max_length=20)
    enable_contact = models.BooleanField(default=1)

    contact_type = models.ForeignKey('contact_types.ContactType')

    def __str__(self):
    	return self.phone_contact