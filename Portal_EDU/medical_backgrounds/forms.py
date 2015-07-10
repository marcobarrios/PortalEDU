from django import forms
from models import MedicalBackGround

class MedicalBackGroundForm(forms.ModelForm):

	class Meta:
		model = MedicalBackGround