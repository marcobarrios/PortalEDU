from django.db import models

class School(models.Model):
    id_school = models.BigIntegerField(primary_key=True)
    name_school = models.CharField(max_length=45)
    phone_school = models.CharField(max_length=45, blank=True)
    address_school = models.CharField(max_length=45, blank=True)
    director_name = models.CharField(max_length=45, blank=True)
    enable_school = models.BooleanField(default=1)