from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required

from ..models import Note

from ..forms import AddNoteForm


def page_not_found(request : HttpRequest, exception : Exception):
    return HttpResponseNotFound(f"<h1>Oops... Something goes wrong...</h1><br>{exception.__class__.__name__}")


@login_required(login_url="/login")
def index(request : HttpRequest):
    return redirect('my_notes')


@login_required(login_url="/login")
def add_note(request : HttpRequest):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                Note.objects.create(**form.cleaned_data, user=request.user)
                return redirect('my_notes')
            except Exception as e:
                form.add_error(None, f"В ходе добавления формы возникло исключение \"{e.__class__.__name__}\": {str(e)}")
    else:
        form = AddNoteForm()

    return render(request, 'notes/main/add_note.html', context={
        'title' : 'Добавление заметки',
        'form' : form
    })


@login_required(login_url="/login")
def user_notes(request : HttpRequest):
    user_notes = Note.objects.filter(user=request.user.id)
    print(user_notes)
    return render(request, 'notes/main/notes.html', context={
            'title' : 'Заметки на Django',
            'user_notes' : user_notes
        })

@login_required(login_url="/login")
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

