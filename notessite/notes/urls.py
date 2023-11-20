from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', authorization, name='login'),
    path('my_notes/', my_notes, name='my_notes'),
    path('my_notes/<int:note_id>/', note),
    path('query_test/', query_test)
]
