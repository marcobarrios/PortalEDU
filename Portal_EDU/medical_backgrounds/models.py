from django.db import models

class MedicalBackGround(models.Model):
    id_medical_background = models.BigIntegerField(primary_key=True, editable=False)
    title_medical_background = models.CharField(max_length=45, blank=True)
    description_medical_background = models.TextField()
    enable_medical_background = models.BooleanField(default=1)