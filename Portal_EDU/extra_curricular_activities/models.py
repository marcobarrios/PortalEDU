from django.db import models

class ExtraCurricularActivity(models.Model):
    id_extra_curricular_activity = models.BigIntegerField(primary_key=True)
    name_activity = models.CharField(max_length=45)
    date_time_activity = models.CharField(max_length=45)
    duration_extra_curricular_activity = models.IntegerField(blank=True, null=True)
    description_activity = models.TextField(blank=True)
    include_parents = models.BooleanField(default=0)
    include_students = models.BooleanField(default=1)
    done_activity = models.BooleanField(default=0)
    enable_extra_curricular_activity = models.BooleanField(default=1)