from django.db import models

class BloodType(models.Model):
    blood_type = models.CharField(max_length=45)
    enable_blood_type = models.BooleanField(default=1)

    def __unicode__(self):
    	return self.blood_type