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
    rooms = Room.objects.order_by('order')
    statuses = Status.objects.all()  # test
    date = DateItem.objects.all()    # test
    print(type(date[0].date_item))   # test


    dates = get_days()
    today = datetime.date.today()

    ctx = {
        'title': title,
        'rooms': rooms,
        'dates': dates,
        'today': today,
        'statuses': statuses,
    }

    return render(request, 'timetable/timetable.html', ctx)


