app_name='mainapp'

from django.urls import path
from django.urls import re_path
import mainapp.views as mainapp

urlpatterns = [
    path('booking/', mainapp.booking, name='booking'),
    # path('book_a_room/', mainapp.book_a_room, name='book')
]