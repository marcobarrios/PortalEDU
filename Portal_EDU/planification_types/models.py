from django.db import models

class PlanificationType(models.Model):
    id_planification_type = models.BigIntegerField(primary_key=True)
    planification_type = models.CharField(max_length=45)
    enable_planification_type = models.BooleanField(default=1)