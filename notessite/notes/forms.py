from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=255, label='Имя пользователя')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(max_length=64, widget=forms.PasswordInput(), label='Пароль')
    password2 = forms.CharField(max_length=64, widget=forms.PasswordInput(), label='Подтвердите пароль')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AuthorizationForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(max_length=64, widget=forms.PasswordInput(), label='Пароль')