# -*- encoding: utf-8 -*-
from django.db import models

class School(models.Model):
    name_school = models.CharField(max_length=45)
    phone_school = models.CharField(max_length=45, blank=True)
    address_school = models.CharField(max_length=45, blank=True)
    director_name_school = models.CharField(max_length=45, blank=True)
    vission_school = models.TextField(blank=True, null=True)
    mission_school = models.TextField(blank=True, null=True)
    enable_school = models.BooleanField(default=1)

    def __unicode__(self):
    	return self.name_school