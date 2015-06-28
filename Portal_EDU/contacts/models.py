from django.db import models

class Contact(models.Model):
    id_contact = models.BigIntegerField(primary_key=True, editable=False)
    phone_contact = models.CharField(max_length=20)
    enable_contact = models.BooleanField(default=1)

    contact_type = models.ForeignKey('contact_types.ContactType')