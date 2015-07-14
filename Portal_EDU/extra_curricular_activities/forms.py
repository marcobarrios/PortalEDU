from django import forms
from models import ExtraCurricularActivity

class ExtraCurricularActivityForm(forms.ModelForm):

	class Meta:
		model = ExtraCurricularActivity
		exclude = ('enable_extra_curricular_activity',)