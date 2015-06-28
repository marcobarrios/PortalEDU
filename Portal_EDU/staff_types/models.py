from django.db import models

class StaffType(models.Model):
    staff_type = models.CharField(max_length=45)
    enable_staff_type = models.BooleanField(default=1)

    def __unicode__(self):
    	return self.staff_type