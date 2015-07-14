from django import forms
from models import Level

class LevelForm(forms.ModelForm):

	class Meta:
		model = Level
		exclude = ('enable_levels',)