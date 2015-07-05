# -*- encoding: utf-8 -*-
from django.db import models

class ExtraCurricularActivity(models.Model):
    name_activity = models.CharField(max_length=45)
    date_activity = models.DateField()
    time_activity = models.TimeField()
    duration_extra_curricular_activity = models.PositiveIntegerField(blank=True, null=True, help_text="En minutos")
    description_activity = models.TextField(blank=True)
    include_parents = models.BooleanField(default=False)
    include_students = models.BooleanField(default=True)
    done_activity = models.BooleanField(default=False)
    enable_extra_curricular_activity = models.BooleanField(default=1)

    staff = models.ForeignKey('staffs.Staff', blank=True, null=True)
    grade = models.ManyToManyField('grades.Grade')
    extra_curricular_activity_type = models.ForeignKey('extra_curricular_activity_types.ExtraCurricularActivityType')

    def __str__(self):
        return self.name_activity