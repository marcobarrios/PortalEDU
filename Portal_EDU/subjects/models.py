from django.db import models

class Subject(models.Model):
    id_subject = models.BigIntegerField(primary_key=True)
    name_csubject= models.CharField(max_length=45, blank=True)
    min_note_subject = models.DecimalField(default=60.00, max_digits=5, decimal_places=2)
    max_note_subject = models.DecimalField(default=100.00, max_digits=5, decimal_places=2)
    enable_subject = models.BooleanField(default=1)
