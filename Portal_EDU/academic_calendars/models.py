from django.db import models

class AcademicCalendar(models.Model):
    id_academic_calendar = models.BigIntegerField(primary_key=True)
    ponderation = models.FloatField()
    description = models.TextField(blank=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    need_file = models.BooleanField(default=0)
    enable_academic_calendar = models.BooleanField(default=1)