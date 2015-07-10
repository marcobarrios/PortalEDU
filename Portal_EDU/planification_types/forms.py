from django import forms
from models import PlanificationType

class PlanificationTypeForm(forms.ModelForm):

	class Meta:
		model = PlanificationType