# -*- encoding: utf-8 -*-
from django.db import models

class PlanificationType(models.Model):
    planification_type = models.CharField(max_length=45)
    enable_planification_type = models.BooleanField(default=1)

    def __unicode__(self):
    	return self.planification_type