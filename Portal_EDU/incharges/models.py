from django.db import models

class Incharge(models.Model):
    id_incharge = models.BigIntegerField(primary_key=True)
    first_name_incharge = models.CharField(max_length=45, blank=True)
    last_name_incharge = models.CharField(max_length=45, blank=True)
    birth_date_incharge = models.CharField(max_length=45, blank=True)
    email_incharge = models.CharField(max_length=45, blank=True)
    home_address_incharge = models.TextField()
    enable_incharge = models.BooleanField(default=1)