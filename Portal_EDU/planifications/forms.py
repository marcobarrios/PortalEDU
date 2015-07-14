from django import forms
from models import Planification

class PlanificationForm(forms.ModelForm):

	class Meta:
		model = Planification
		exclude = ('enable_planification',)