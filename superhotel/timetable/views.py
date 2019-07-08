from django.shortcuts import render
from .models import Room, DateItem, Status

import datetime

def get_days(days_qty=6, date=None):
    one_day = datetime.timedelta(1) # we will add one day in cycle
    result = []

    if date == None:
        date = datetime.date.today()
        result.append(str(date))

    for _ in range(days_qty):
        date+=one_day
        result.append(str(date))

    return result


def show_table(request):
    title = 'Timetable'
    rooms = Room.objects.all()
    date = DateItem.objects.all()
    today = get_days()

    ctx = {
        'title': title,
        'rooms': rooms,
        # 'dates': dates,
        'today': today,}

    return render(request, 'timetable/timetable.html', ctx)
