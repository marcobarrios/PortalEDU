from django import forms
from models import StaffType

class StaffTypeForm(forms.ModelForm):

	class Meta:
		model = StaffType
		exclude = ('enable_staff_type',)
