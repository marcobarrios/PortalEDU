from django.db import models

class Planification(models.Model):
    id_planification = models.BigIntegerField(primary_key=True, editable=False)
    planification_file = models.FileField(upload_to='planifitacion_files/%Y/%m/%d/', blank=True)
    description_planification = models.TextField(blank=True, null=True)
    enable_planification = models.BooleanField(default=1)

    planifitacion_type = models.ForeignKey('planification_types.PlanificationType')