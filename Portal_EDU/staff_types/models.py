from django.db import models

class StaffType(models.Model):
    id_staff_type = models.BigIntegerField(primary_key=True, editable=False)
    staff_type = models.CharField(max_length=45)
    enable_staff_type = models.BooleanField(default=1)