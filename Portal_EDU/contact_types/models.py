from django.db import models

class ContactType(models.Model):
	id_contact_type = models.BigIntegerField(primary_key=True)
	contact_type = models.CharField(max_length=45)
	enable_contact_type = models.BooleanField(default=1)