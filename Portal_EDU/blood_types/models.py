from django.db import models

class BloodType(models.Model):
    id_blood_type = models.BigIntegerField(primary_key=True, editable=False)
    blood_type = models.CharField(max_length=45)
    enable_blood_type = models.BooleanField(default=1)