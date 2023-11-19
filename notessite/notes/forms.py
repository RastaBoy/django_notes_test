from django import forms
from .models import *


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255, label='Имя пользователя')
    email = forms.EmailField(label='Email')
    password = forms.CharField(max_length=64, widget=forms.PasswordInput(), label='Пароль') # Этот пароль должен формироваться
