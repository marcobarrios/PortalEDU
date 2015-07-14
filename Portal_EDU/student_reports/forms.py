from django import forms
from models import StudentReport

class StudentReportForm(forms.ModelForm):

	class Meta:
		model = StudentReport
		exclude = ('enable_student_report',)
