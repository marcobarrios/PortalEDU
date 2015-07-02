from django.db import models

class GradeName(models.Model):
    gradename = models.CharField(max_length=45)
    enable_grade_name = models.BooleanField(default=1)

    def __str__(self):
    	return self.gradename