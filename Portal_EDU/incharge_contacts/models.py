# -*- encoding: utf-8 -*-
from django.db import models

class InchargeContact(models.Model):
	contact_incharge = models.CharField(max_length=45)
	contact_extension_incharge = models.CharField(max_length=10, blank=True, null=True)
	enable_incharge_contact = models.BooleanField(default=1)

	incharge = models.ForeignKey('incharges.Incharge')

	def __unicode__(self):
		return self.contact_incharge + " ext " + self.contact_extension_incharge