from django import forms
from models import BloodType

class BloodTypeForm(forms.ModelForm):

	class Meta:
		model = BloodType

