from django.db import models

class Task(models.Model):
    id_task = models.BigIntegerField(primary_key=True)
    title_task = models.CharField(max_length=45, blank=True, null=True)
    description_task = models.TextField(blank=True, null=True)  
    file_task = models.FileField(blank=True) 
	delivered_date = models.DateTimeField(blank=True, null=True) 
    ponderation_task = models.FloatField(blank=True, null=True)
    checked = models.IntegerField(blank=True, null=True)
    teacher_commentary_task = models.TextField(blank=True) 
    enable_task = models.BooleanField(default=1) 