from django import forms
from models import StudentControlList

class StudentControlListForm(forms.ModelForm):

	class Meta:
		model = StudentControlList
		exclude = ('enable_student_control_list',)
