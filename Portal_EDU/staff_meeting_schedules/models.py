from django.db import models

class StaffMeetingSchedule(models.Model):
    date_time_init_staff_meeting_schedule = models.DateTimeField()
    date_time_end_staff_meeting_schedule = models.DateTimeField()
    enable_staff_meeting_schedule = models.BooleanField(default=1)

    staff = models.ForeignKey('staffs.Staff')