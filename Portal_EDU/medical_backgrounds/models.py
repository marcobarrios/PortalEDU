from django.db import models

class MedicalBackGround(models.Model):
    id_medical_background = models.BigIntegerField(primary_key=True)
    medical_background = models.TextField()
    enable_medical_background = models.BooleanField(default=1)