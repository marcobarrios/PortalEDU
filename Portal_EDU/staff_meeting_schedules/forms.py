from django import forms
from models import StaffMeetingSchedule

class StaffMeetingScheduleForm(forms.ModelForm):

	class Meta:
		model = StaffMeetingSchedule
		exclude = ('enable_staff_meeting_schedule',)
