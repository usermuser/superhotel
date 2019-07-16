from django.shortcuts import render
from .models import Room, DateItem #, Status

import datetime

def get_days(days_qty=2, date=None):
    one_day = datetime.timedelta(1) # we will add one day in cycle
    result = []

    if date == None:
        date = datetime.date.today()
        result.append(str(date))

    for _ in range(days_qty):
        date += one_day
        result.append(str(date))

    return result   # ['2019-07-11', '2019-07-12', '2019-07-13']


# print(get_days(days_qty=1))

# all_dates = DateItem.objects.all().order_by('date_item')
# all_rooms = Room.objects.order_by('order')

# for room in all_rooms:
#     room_dates = all_dates.filter(room_id=room.id)
#     print(room_dates)


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
    if start_date == None:
        start_date = datetime.date.today()
        print(type(start_date), start_date)
    else:
        start_date=start_date

    rooms = Room.objects.order_by('order')
    dates = DateItem.objects.order_by('date_item').filter(date_item__gte=start_date)[:3]
    # timetable = dates.filter(room_id=rooms[0].id).order_by('date_item')[:2]
    # print(timetable)

    ctx = {
        'title': title,
        'rooms': rooms,
        'dates': dates,
    }

    return render(request, 'timetable/bst.html', ctx)


