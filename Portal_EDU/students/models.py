from django.db import models

class Student(models.Model):
    id_student = models.BigIntegerField(primary_key=True, editable=False)
    image_student = models.ImageField(upload_to='student_images/%Y/%m/%d/', blank=True)
    code_student = models.CharField(max_length=45, blank=True) 
    first_name_student = models.CharField(max_length=45) 
    last_name_student = models.CharField(max_length=45) 
    birth_date_student = models.DateField() 
    email_student = models.EmailField(max_length=254, blank=True)
    home_address_student = models.TextField(blank=True, null=True)
    enable_student = models.BooleanField(default=1)

    genre = models.ForeignKey('genres.Genre')
    blood_type = models.ForeignKey('blood_types.BloodType')
    incharges = models.ManyToManyField('incharges.Incharge')
    medical_backgrounds = models.ManyToManyField('medical_backgrounds.MedicalBackground')
    contacts = models.ManyToManyField('contacts.Contact')