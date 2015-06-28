from django.db import models

class StaffActivity(models.Model):
    id_staff_activity = models.BigIntegerField(primary_key=True, editable=False)
    name_staff_activity = models.CharField(max_length=45)
    date_time_staff_activity = models.DateTimeField(blank=True, null=True)
    descripcion_staff_activity = models.CharField(max_length=255, blank=True)
    done_staff_activity = models.IntegerField(blank=True, null=True)
    enable_staff_activity = models.BooleanField(default=1)