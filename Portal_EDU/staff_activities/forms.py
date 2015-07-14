from django import forms
from models import StaffActivity

class StaffActivityForm(forms.ModelForm):

	class Meta:
		model = StaffActivity
		exclude = ('enable_staff_activity',)
