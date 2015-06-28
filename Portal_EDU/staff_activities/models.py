from django.db import models

class StaffActivity(models.Model):
    name_staff_activity = models.CharField(max_length=45)
    date_time_staff_activity = models.DateTimeField(blank=True, null=True)
    descripcion_staff_activity = models.CharField(max_length=255, blank=True)
    done_staff_activity = models.IntegerField(blank=True, null=True)
    enable_staff_activity = models.BooleanField(default=1)

    def __unicode__(self):
    	return self.name_staff_activity