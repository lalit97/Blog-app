from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, get_user_model


class RegisterForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    confirm_password = forms.CharField(max_length=20)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)

    def check(self):
        pass 
        
