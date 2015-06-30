from django.db import models

class Planification(models.Model):
    title_planification = models.CharField(max_length=45, blank=True)
    description_planification = models.TextField(blank=True, null=True)
    planification_file = models.FileField(upload_to='planifitacion_files/%Y/%m/%d/', blank=True)
    enable_planification = models.BooleanField(default=1)

    course = models.ForeignKey('courses.Course')
    planifitacion_type = models.ForeignKey('planification_types.PlanificationType')

    def __unicode__(self):
    	return self.title_planification