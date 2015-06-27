from django.db import models

class ExtraCurricularActivityType(models.Model):
    id_extra_curricular_activity_type = models.BigIntegerField(primary_key=True)
    extra_curricular_activity_type = models.CharField(max_length=45)
    enable_extra_curricular_activity_type = models.BooleanField(default=1)