from django.db import models

class ClassRoom(models.Model):
	classroom = models.CharField(max_length=10)
	enable_classroom = models.BooleanField(default=1)

	def __str__(self):
		return self.classroom