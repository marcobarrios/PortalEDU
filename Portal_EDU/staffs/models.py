# -*- encoding: utf-8 -*-
from django.db import models

class Staff(models.Model):
    image_staff = models.ImageField(upload_to='staff_images/%Y/%m/%d/', blank=True, null=True)
    code_staff = models.CharField(max_length=45, blank=True) 
    first_name_staff = models.CharField(max_length=45) 
    last_name_staff = models.CharField(max_length=45) 
    birth_date_staff = models.DateField(blank=True)
    email_staff = models.EmailField(max_length=254, blank=True)
    home_address_staff = models.TextField(blank=True, null=True)
    neighborhood_staff = models.TextField(blank=True, null=True)
    identification_document_staff = models.CharField(max_length=20, blank=True)
    nit_staff = models.CharField(max_length=15, blank=True)
    igss_afiliation_number_staff = models.CharField(max_length=25, blank=True)
    teaching_certificate_staff = models.CharField(max_length=45, blank=True)
    title_staff = models.CharField(max_length=45, blank=True)
    cv_file_staff = models.FileField(upload_to='staff_cv_files/%Y/%m/%d/', blank=True)
    enable_staff = models.BooleanField(default=1)

    staff_type = models.ForeignKey('staff_types.StaffType')
    genre = models.ForeignKey('genres.Genre')
    blood_type = models.ForeignKey('blood_types.BloodType')
    medical_backgrounds = models.ManyToManyField('medical_backgrounds.MedicalBackground', blank=True, null=True)
    contacts = models.ManyToManyField('contacts.Contact', blank=True, null=True)

    def __str__(self):
        return self.last_name_staff + ", " + self.first_name_staff