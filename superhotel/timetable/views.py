from django.shortcuts import render
from .models import Room, DateItem, Status

import datetime

now=datetime.datetime.now()
today=now.strftime('%Y-%m-%d %w')

print(today)

def show_table(request):
    title = 'Timetable'
    rooms = Room.objects.all()
    dates = DateItem.objects.all()

    ctx = {
        'title': title,
        'rooms': rooms,
        'dates': dates,}

    return render(request, 'timetable/timetable.html', ctx)
