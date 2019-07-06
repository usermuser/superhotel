from django.urls import path
from timetable import views as timetable


app_name = 'timetable'

from django.urls import path
import timetable.views as timetable

urlpatterns = [
    path('', timetable.show_table, name ='show table'),
]