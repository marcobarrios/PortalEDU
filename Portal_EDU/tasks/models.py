from django.db import models

class Task(models.Model):
    id_task = models.BigIntegerField(primary_key=True)
	delivered_date_task = models.DateTimeField(blank=True, null=True) 
    checked_task = models.IntegerField(blank=True, null=True)
    file_task = models.FileField(blank=True) 
    teacher_commentary_task = models.TextField(blank=True) 
    enable_task = models.BooleanField(default=1) 