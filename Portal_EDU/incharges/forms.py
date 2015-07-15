from django import forms
from models import Incharge
from django.contrib.auth.models import User

class InchargeForm(forms.ModelForm):

	class Meta:
		model = Incharge
		exclude = ('enable_incharge',)

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
