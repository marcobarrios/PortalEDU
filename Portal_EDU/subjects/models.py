# -*- encoding: utf-8 -*-
from django.db import models

class Subject(models.Model):
    name_subject= models.CharField(max_length=45)
    min_note_subject = models.DecimalField(default=60.00, max_digits=5, decimal_places=2)
    max_note_subject = models.DecimalField(default=100.00, max_digits=5, decimal_places=2)
    enable_subject = models.BooleanField(default=1)

    def __str__(self):
    	return self.name_subject
