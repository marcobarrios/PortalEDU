from django import forms
from models import StaffEntranceSchedule

class StaffEntranceScheduleForm(forms.ModelForm):

	class Meta:
		model = StaffEntranceSchedule
		exclude = ('enable_staff_entrance_schedule',)
