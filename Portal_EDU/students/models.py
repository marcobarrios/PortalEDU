# -*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings

class Student(models.Model):
    image_student = models.ImageField(upload_to='files/images/students/%Y/%m/%d/', blank=True)
    code_student = models.CharField(max_length=45, blank=True) 
    first_name_student = models.CharField(max_length=45) 
    last_name_student = models.CharField(max_length=45) 
    birth_date_student = models.DateField(max_length=15) 
    email_student = models.EmailField(max_length=254, blank=True)
    home_address_student = models.CharField(max_length=80, blank=True, null=True)
    neighborhood_student = models.CharField(max_length=50, blank=True, null=True)
    enable_student = models.BooleanField(default=1)

    genre = models.ForeignKey('genres.Genre')
    blood_type = models.ForeignKey('blood_types.BloodType')
    incharges = models.ManyToManyField('incharges.Incharge')
    medical_backgrounds = models.ManyToManyField('medical_backgrounds.MedicalBackground', blank=True, null=True)
    contacts = models.ManyToManyField('contacts.Contact')
    grade = models.ForeignKey('grades.Grade', blank=True, null=True)
    authentication = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True)

    def __str__(self):
        return self.last_name_student + ", " + self.first_name_student