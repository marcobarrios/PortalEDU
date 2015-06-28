from django.db import models

class ExtraCurricularActivity(models.Model):
    name_activity = models.CharField(max_length=45)
    date_time_activity = models.CharField(max_length=45)
    duration_extra_curricular_activity = models.PositiveIntegerField(blank=True, null=True)
    description_activity = models.TextField(blank=True)
    include_parents = models.BooleanField(default=0)
    include_students = models.BooleanField(default=1)
    done_activity = models.BooleanField(default=0)
    enable_extra_curricular_activity = models.BooleanField(default=1)

    staff = models.ForeignKey('staffs.Staff')
    extra_curricular_activity_type = models.ForeignKey('extra_curricular_activity_types.ExtraCurricularActivityType')

    def __unicode__(self):
        return self.name_activity