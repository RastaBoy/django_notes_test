from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.urls import reverse_lazy

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

from ..forms import *





class RegisterUserView(CreateView):
    form_class = RegistrationForm
    template_name = 'notes/authorization/register.html'
    success_url = reverse_lazy('login')


def authorization(request : HttpRequest):
    form = RegistrationForm()

    return render(request, 'notes/authorization/login.html', context={
        'title' : 'Авторизация',
        'form' : form
    })


# def test_page(request : HttpRequest):
#     if request.method == 'POST':
#         form = AuthorizationForm(request.POST)
#         if form.is_valid():
#             try:
#                 user = AuthorizationController().register_user(RegisterRequest(**form.cleaned_data))
#                 # Возвращать редирект на страницу авторизации
#             except AuthorizationException as ex:
#                 form.add_error(None, str(ex))
    
#     else:
#         form = AuthorizationForm()

#     return render(request, 'notes/tests.html', context={
#         'title' : 'Страница для тестов',
#         'form' : form
#     })