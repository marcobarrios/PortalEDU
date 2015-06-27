from django.db import models

class Staff(models.Model):
    id_staff = models.BigIntegerField(primary_key=True) 
    image_staff = models.ImageField(blank=True) 
    code_staff = models.CharField(max_length=45, blank=True) 
    first_name_staff = models.CharField(max_length=45) 
    last_name_staff = models.CharField(max_length=45) 
    birth_date_staff = models.CharField(max_length=45, blank=True)
    email_staff = models.CharField(max_length=45, blank=True)
    home_address_staff = models.TextField(blank=True, null=True)
    enable_staff = models.BooleanField(default=1)