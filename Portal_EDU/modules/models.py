# -*- encoding: utf-8 -*-
from django.db import models

class Module(models.Model):
    module_name = models.CharField(max_length=45)
    enable_module = models.BooleanField(default=1)

    def __str__(self):
    	return self.module_name