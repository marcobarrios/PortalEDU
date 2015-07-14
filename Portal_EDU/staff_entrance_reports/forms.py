from django import forms
from models import StaffEntranceReport

class StaffEntranceReportForm(forms.ModelForm):

	class Meta:
		model = StaffEntranceReport
		exclude = ('enable_staff_entrance_report',)
