from django import forms
from models import GradeName

class GradeNameForm(forms.ModelForm):

	class Meta:
		model = GradeName
		exclude = ('enable_grade_name',)