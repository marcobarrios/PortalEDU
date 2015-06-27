from django.db import models

class AcademicCalendar(models.Model):
    id_academic_calendar = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=45, blank=True)
    description = models.TextField(blank=True)
    ponderation = models.FloatField(default=0.0)
    grade = models.FloatField(default=0.0, blank=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    need_file = models.BooleanField(default=0)
    enable_academic_calendar = models.BooleanField(default=1)