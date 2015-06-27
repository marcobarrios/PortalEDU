from django.db import models

class InchargeType(models.Model):
    id_incharge_type = models.BigIntegerField(primary_key=True)
    incharge_type = models.CharField(max_length=45)
    enable_incharge_type = models.BooleanField(default=1)