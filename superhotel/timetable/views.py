from django.shortcuts import render
from .models import Room, DateItem

import datetime


def get_days(days_qty=2, date=None):
    one_day = datetime.timedelta(1) # we will add one day in cycle
    result = []

    if date is None:
        date = datetime.date.today()
        result.append(str(date))

    for _ in range(days_qty):
        date += one_day
        result.append(str(date))

    return result   # ['2019-07-11', '2019-07-12', '2019-07-13']


def show_table(request):
    title = 'Timetable'
    rooms = Room.objects.order_by('order')
    dates = DateItem.objects.order_by('date_item')
    timetable = dates.filter(room_id=rooms[0].id).order_by('date_item')[:2]
    print(timetable)

    ctx = {
        'title': title,
        'rooms': rooms,
        'dates': dates,
    }

    return render(request, 'timetable/timetable.html', ctx)


def show_week(request, start_date=None):
    title = 'Timetable'
    if start_date is None:
        start_date = datetime.date.today()
        # print(type(start_date), start_date)
    else:
        start_date=start_date

    rooms = Room.objects.order_by('order')
    all_dates = DateItem.objects.all()
    dates = all_dates.order_by('date_item').filter(date_item__gte=start_date)[:3]
    distinct_dates = all_dates.order_by().values('date_item').distinct()
    print(distinct_dates)

    ctx = {
        'title': title,
        'rooms': rooms,
        'dates': dates,
        'distinct_dates': distinct_dates,
    }

    return render(request, 'timetable/timetable.html', ctx)


