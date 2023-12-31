from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('my_notes/', user_notes, name='my_notes'),
    path('my_notes/add_note', add_note, name='add_note'),
    path('my_notes/<int:note_id>/', note),
    path('query_test/', query_test)
]
