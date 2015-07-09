from django import forms
from models import InchargeAppointment

class InchargeAppointmentForm(forms.ModelForm):

	class Meta:
		model = InchargeAppointment
		exclude = ('enable_incharge_appointment','status_incharge_appointment','confirmation_incharge_appointment',)