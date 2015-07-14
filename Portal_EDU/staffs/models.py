# -*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings

class Staff(models.Model):
    image_staff = models.ImageField(upload_to='files/images/staffs/%Y/%m/%d/', blank=True, null=True)
    code_staff = models.CharField(max_length=45, blank=True) 
    first_name_staff = models.CharField(max_length=45) 
    last_name_staff = models.CharField(max_length=45) 
    birth_date_staff = models.DateField(max_length=15 ,blank=True)
    email_staff = models.EmailField(max_length=254, blank=True)
    home_address_staff = models.CharField(max_length=80, blank=True, null=True)
    neighborhood_staff = models.CharField(max_length=50, blank=True, null=True)
    identification_document_staff = models.CharField(max_length=20, blank=True)
    nit_staff = models.CharField(max_length=15, blank=True)
    igss_afiliation_number_staff = models.CharField(max_length=25, blank=True)
    teaching_certificate_staff = models.CharField(max_length=45, blank=True)
    profession_staff = models.CharField(max_length=45, blank=True)
    cv_file_staff = models.FileField(upload_to='files/staff_cvn/%Y/%m/%d/', blank=True)
    enable_staff = models.BooleanField(default=1)

    staff_type = models.ForeignKey('staff_types.StaffType')
    genre = models.ForeignKey('genres.Genre')
    blood_type = models.ForeignKey('blood_types.BloodType')
    medical_backgrounds = models.ManyToManyField('medical_backgrounds.MedicalBackground', blank=True, null=True)
    authentication_staff = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True)

    def __str__(self):
        return self.last_name_staff + ", " + self.first_name_staff