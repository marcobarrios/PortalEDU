from django.db import models

class Task(models.Model):
    delivered_date_task = models.DateTimeField(auto_now=True)
    checked_task = models.BooleanField(default=0)
    file_task = models.FileField(upload_to='task_files/%Y/%m/%d/', blank=True)
    teacher_commentary_task = models.TextField(blank=True) 
    enable_task = models.BooleanField(default=1) 

    student = models.ForeignKey('students.Student')
    academic_calendar = models.ForeignKey('academic_calendars.AcademicCalendar')