from django import forms
from models import ExtraCurricularActivityType

class ExtraCurricularActivityTypeForm(forms.ModelForm):

	class Meta:
		model = ExtraCurricularActivityType
		exclude = ('enable_extra_curricular_activity_type',)