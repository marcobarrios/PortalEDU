from django.db import models

class GradeName(models.Model):
    id_grade_name = models.BigIntegerField(primary_key=True)
    gradename = models.CharField(max_length=45)
    enable_grade_name = models.BooleanField(default=1)