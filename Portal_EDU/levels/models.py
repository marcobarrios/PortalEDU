# -*- encoding: utf-8 -*-
from django.db import models

class Level(models.Model):
    name_level = models.CharField(max_length=45)
    sub_name_level = models.CharField(max_length=45, blank=True, null=True)
    enable_levels = models.BooleanField(default=1)

    def __str__(self):
    	return self.name_level + " " + self.sub_name_level