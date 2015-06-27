from django.db import models

class Contact(models.Model):
    id_contact = models.BigIntegerField(primary_key=True)
    phone_contact = models.CharField(max_length=20)
    enable_contact = models.BooleanField(default=1)