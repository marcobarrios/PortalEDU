from django.db import models

class AcademicCalendar(models.Model):
    id_academic_calendar = models.BigIntegerField(primary_key=True, editable=False)
    title = models.CharField(max_length=45, blank=True)
    description = models.TextField(blank=True)
    ponderation = models.DecimalField(default=0.0, max_digits=4, decimal_places=2)
    grade = models.DecimalField(default=0.0, max_digits=4, decimal_places=2)
    delivery_date = models.DateTimeField(blank=True, null=True)
    need_file = models.BooleanField(default=0)
    enable_academic_calendar = models.BooleanField(default=1)

    assignment = models.ForeignKey('assignments.Assignment')
    course = models.ForeignKey('courses.Course')