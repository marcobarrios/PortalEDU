# -*- encoding: utf-8 -*-
from django.db import models

class ContactType(models.Model):
	contact_type = models.CharField(max_length=45)
	enable_contact_type = models.BooleanField(default=1)

	def __str__(self):
		return self.contact_type
