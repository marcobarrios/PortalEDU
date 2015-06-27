from django.db import models

class Grade(models.Model):
	id_grade = models.BigIntegerField(primary_key=True)
	enable_grade = models.BooleanField(default=1)

	grade_name = models.ForeignKey('grade_names.GradeName')
	section = models.ForeignKey('sections.Section')
	staff = models.ForeignKey('staffs.Staff')
	level = models.ForeignKey('levels.Level')
	extra_curricular_activities = models.ManyToManyField('extra_curricular_activities.ExtraCurricularActivity')