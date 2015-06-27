from django.db import models

class Grade(models.Model):
	id_grade = models.BigIntegerField(primary_key=True)
	enable_grade = models.BooleanField(default=1)
