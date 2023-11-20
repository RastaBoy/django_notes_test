from django.shortcuts import render
from django.http import HttpRequest

from ..forms import *

from ..controllers.auth import AuthorizationController, AuthorizationRequest, RegisterRequest, RegisterException, AuthorizationException


def register(request : HttpRequest):
    return render(request, 'notes/authorization/register.html', context={
        'title' : 'Регистрация'
    })

def test_page(request : HttpRequest):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = AuthorizationController().register_user(RegisterRequest(**form.cleaned_data))
                # Возвращать редирект на страницу авторизации
            except RegisterException as ex:
                form.add_error(None, str(ex))
    
    else:
        form = RegistrationForm()

    return render(request, 'notes/tests.html', context={
        'title' : 'Страница для тестов',
        'form' : form
    })