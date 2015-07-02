from django.db import models

class ExtraCurricularActivityType(models.Model):
    extra_curricular_activity_type = models.CharField(max_length=45)
    enable_extra_curricular_activity_type = models.BooleanField(default=1)

    def __str__(self):
    	return self.extra_curricular_activity_type