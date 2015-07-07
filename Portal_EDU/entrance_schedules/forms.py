from django import forms
from models import EntranceSchedule

class EntranceScheduleForm(forms.ModelForm):

	class Meta:
		model = EntranceSchedule