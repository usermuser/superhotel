from django.urls import path, re_path
from timetable import views as timetable


app_name = 'timetable'

from django.urls import path
import timetable.views as timetable

urlpatterns = [
    path('', timetable.show_table, name ='show table'),
    path('show_week/', timetable.show_week, name ='show week'),
    # re_path('show_table/', timetable.show_week, name ='show week'),
    # ^20(1|2)\d\-(0|1)\d\-(0|1|2|3)\d$
    # re_path(r'^20(1|2)\d\-(0|1)\d\-(0|1|2|3)\d$', timetable.show_table, name='show week'),
]