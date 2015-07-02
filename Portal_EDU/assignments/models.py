# -*- encoding: utf-8 -*-
from django.db import models

class Assignment(models.Model):
    assignment_name = models.CharField(max_length=45)
    enable_assigment = models.BooleanField(default=1)

    def __str__(self):
        return self.assignment_name
