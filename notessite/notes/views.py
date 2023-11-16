from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound


# Create your views here.
def index(request : HttpRequest):
    return render(request, 'notes/main_page.html', context={
        'title' : 'Заметки на Django',
        'objects' : [
            'Vasya',
            'Petya',
            'Pupa'
        ]
    })


def note(request : HttpRequest, note_id : int):
    if note_id >5:
        return redirect('home')
    return HttpResponse(f"<h1>Страница приложения Note {note_id}.</h1>")


def query_test(request : HttpRequest):
    response_string = "<h1>Query Test Result:</h1><br>"
    if request.GET:
        for key, value in request.GET.items():
            response_string += f"<h2>{key} : {value}</h2><br>"
    return HttpResponse(response_string)


def page_not_found(request : HttpRequest, exception : Exception):
    return HttpResponseNotFound(f"<h1>Oops... Something goes wrong...</h1><br>{exception.__class__.__name__}")