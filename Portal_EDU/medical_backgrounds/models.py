# -*- encoding: utf-8 -*-
from django.db import models

class MedicalBackGround(models.Model):
    title_medical_background = models.CharField(max_length=45)
    description_medical_background = models.TextField(blank=True, null=True)
    treatment_medical_background = models.TextField(blank=True, null=True)
    enable_medical_background = models.BooleanField(default=1)

    def __str__(self):
    	return self.title_medical_background