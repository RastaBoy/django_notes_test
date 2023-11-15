from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def index_notes(request : HttpRequest):
    return HttpResponse("<h1>Страница приложения Notes.</h1>")


# def index_notes(request : HttpRequest):
#     return HttpResponse("<h1>Страница приложения Notes.</h1>")