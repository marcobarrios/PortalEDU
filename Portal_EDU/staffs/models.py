from django.db import models

class Staff(models.Model):
    id_staff = models.BigIntegerField(primary_key=True) 
    image_staff = models.ImageField(blank=True null=True) 
    code_staff = models.CharField(max_length=45, blank=True) 
    first_name_staff = models.CharField(max_length=45) 
    last_name_staff = models.CharField(max_length=45) 
    birth_date_staff = models.CharField(max_length=45, blank=True)
    email_staff = models.CharField(max_length=45, blank=True)
    home_address_staff = models.TextField(blank=True, null=True)
    identification_document_staff = models.CharField(max_length=20, blank=True)
    nit_staff = models.CharField(max_length=15, blank=True)
    igss_afiliation_number_staff = models.CharField(max_length=25, blank=True)
    teaching_certificate_staff = models.CharField(max_length=45, blank=True)
    title_staff = models.CharField(max_length=45, blank=True)
    cv_file_staff = models.FileField(blank=True)
    enable_staff = models.BooleanField(default=1)