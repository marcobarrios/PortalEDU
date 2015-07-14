from django import forms
from models import StaffAppointment

class StaffAppointmentForm(forms.ModelForm):

	class Meta:
		model = StaffAppointment
		exclude = ('enable_staff_appointment',)
