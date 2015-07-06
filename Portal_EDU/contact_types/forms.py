from django import forms
from models import ContactType

class ContactTypeForm(forms.ModelForm):

	class Meta:
		model = ContactType
