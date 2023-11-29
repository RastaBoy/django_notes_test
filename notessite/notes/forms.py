from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import *


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=255, label='Имя пользователя')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(max_length=64, widget=forms.PasswordInput(), label='Пароль')
    password2 = forms.CharField(max_length=64, widget=forms.PasswordInput(), label='Подтвердите пароль')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(max_length=64, widget=forms.PasswordInput(), label='Пароль')

    class Meta:
        model = User
        fields = ('username', 'password')


class AddNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Заголовок'
        self.fields['content'].label = 'Заметка'

    class Meta:
        model = Note
        fields = ('title', 'content')