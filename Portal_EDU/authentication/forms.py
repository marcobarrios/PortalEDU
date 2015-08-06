# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder': 'Usuario'}),
            'password'    : forms.TextInput(attrs = {'placeholder': 'Contraseña', 'type': 'password' }),
        }