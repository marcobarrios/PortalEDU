from django import forms
from models import Staff
from django.contrib.auth.models import User

class StaffForm(forms.ModelForm):

	class Meta:
		model = Staff
		exclude = ('enable_staff',)

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
