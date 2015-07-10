from django import forms
from models import InchargeType

class InchargeTypeForm(forms.ModelForm):

	class Meta:
		model = InchargeType