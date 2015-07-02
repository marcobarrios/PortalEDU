from django.db import models

class InchargeType(models.Model):
    incharge_type = models.CharField(max_length=45)
    enable_incharge_type = models.BooleanField(default=1)

    def __str__(self):
    	return self.incharge_type
