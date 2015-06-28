from django.db import models

class Assignment(models.Model):
    id_assignment = models.BigIntegerField(primary_key=True, editable=False)
    assignment_name = models.CharField(max_length=45)
    enable_assigment = models.BooleanField(default=1)