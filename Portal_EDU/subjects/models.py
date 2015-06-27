from django.db import models

class Subject(models.Model):
    id_subject = models.BigIntegerField(primary_key=True)
    name_csubject= models.CharField(max_length=45, blank=True)
    min_note_subject = models.IntegerField(blank=True, null=True)
    max_note_subject = models.IntegerField(blank=True, null=True)
    enable_subject = models.BooleanField(default=1)
