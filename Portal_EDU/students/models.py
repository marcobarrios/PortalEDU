from django.db import models

class Student(models.Model):
    id_student = models.BigIntegerField(primary_key=True)
    image_student = models.ImageField(blank=True) 
    code_student = models.CharField(max_length=45, blank=True) 
    first_name_student = models.CharField(max_length=45) 
    last_name_student = models.CharField(max_length=45) 
    birth_date_student = models.DateField() 
    email_student = models.CharField(max_length=45, blank=True) 
    home_address_student = models.TextField(blank=True, null=True)
    enable_student = models.BooleanField(default=1)