from django import forms
from models import AcademicCalendar

class AcademicCalendarForm(forms.ModelForm):

	class Meta:
		model = AcademicCalendar
		exclude = ('enable__academic_calendar',)
