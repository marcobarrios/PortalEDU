from django.db import models

class Grade(models.Model):
	id_grade = BigIntegerField(primary_key=True)
	enable_grade = BooleanField(default=1)
