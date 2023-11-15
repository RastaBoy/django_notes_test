from django.urls import path

from .views import *


urlpatterns = [
    path('', index_notes, name='home'),
    path('notes/<int:note_id>/', note),
    path('query_test/', query_test)
]
