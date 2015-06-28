from django.db import models

class ClassRoom(models.Model):
	id_classroom = models.BigIntegerField(primary_key=True, editable=False)
	classroom = models.CharField(max_length=10)
	enable_classroom = models.BooleanField(default=1)