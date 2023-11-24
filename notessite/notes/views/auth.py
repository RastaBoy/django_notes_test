from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy

from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

from .abc import NotesContextOrganizer

from ..forms import *




class RegisterUserView(NotesContextOrganizer, CreateView):
    form_class = RegistrationForm
    template_name = 'notes/authentication/register.html'
    success_url = reverse_lazy('login')
    title = 'Регистрация'


    def form_valid(self, form: Any) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        return redirect('my_notes')


class LoginUserView(NotesContextOrganizer, LoginView):
    from_class = LoginUserForm
    template_name = 'notes/authentication/login.html'
    title = 'Авторизация'

    def get_success_url(self) -> str:
        return reverse_lazy('my_notes')




def logout_user(request : HttpRequest):
    logout(request)
    return redirect('login')