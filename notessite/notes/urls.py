from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('my_notes/', my_notes, name='my_notes'),
    path('my_notes/<int:note_id>/', note),
    path('query_test/', query_test)
]
