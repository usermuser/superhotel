from django.db import models


# class Hotel(models.Model):
#     nameOfHotel = models.CharField(verbose_name='Название отеля', max_length=100)
#     tax = models.PositiveIntegerField(verbose_name='Налог')

class Room(models.Model):
    name = models.CharField(verbose_name='имя', max_length=55, unique=True)
    price = models.PositiveIntegerField(verbose_name='Цена')
    # adults = models.PositiveIntegerField(verbose_name='Кол-во взрослых', default=0)
    # kids = models.PositiveIntegerField(verbose_name='Кол-во детей', default=0)
    # infants = models.PositiveIntegerField(verbose_name='Кол-во младенцев', default=0)
    # extraPerson = models.PositiveIntegerField(verbose_name='Цена за доп. человека', default=0)
    image1 = models.ImageField(upload_to='rooms_img/%Y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='rooms_img/%Y/%m/%d', blank=True)
    description = models.TextField(verbose_name='описание номера', blank=True)
    order = models.PositiveIntegerField(verbose_name='порядок') # при отображении на расписании

    class Meta:
        verbose_name = 'номер'
        verbose_name_plural = 'номера'

    def __str__(self):
        return self.name

# class DateItem(models.Model):
#     date_item = models.DateField('дата бронирования')
#     # check_in = models.DateField(verbose_name='дата заезда')
#     # check_out = models.DateField(verbose_name='дата выезда')
#     room = models.ForeignKey('room', on_delete=models.CASCADE,)
#     is_busy = models.BooleanField(verbose_name='занят', default=False)
#
#     class Meta:
#         verbose_name = 'дата бронирования'
#         verbose_name_plural = 'даты бронирования'
#
#     def __str__(self):
#         return str(self.date_item)


#таблица которая хранит в себе все введеные тексты из формы при заполнении(пользователем в админке не заполняется)
# class Data(models.Model):
#     nameOfText = models.CharField(max_length=70)
#     valueOfText = models.CharField(max_length=5000)
#
# class TableTime(models.Model):
#     field = models.CharField(max_length=100)


class DateItem(models.Model):
    status_to_choose = [['f','свободен'], ['b','занят']]
    date_item = models.DateField('дата бронирования')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='date')
    status = models.CharField(max_length=1, choices=status_to_choose, default='f')

    class Meta:
        verbose_name = 'дата бронирования'
        verbose_name_plural = 'даты бронирования'

    def __str__(self):
        return str(self.date_item)


# class Status(models.Model):
    # def __init__(self):
    #     super(Status, self).__init__()
    # _status = _get_status

    # is_busy = models.BooleanField(verbose_name='занят', default=False)
    # date = models.ForeignKey(DateItem, on_delete=models.CASCADE, related_name='status')

    # def _get_status(self):
    #     if self.is_busy:
    #         return 'занят'
    #     return 'свободен'

    # class Meta:
    #     verbose_name = 'cтатус'
    #     verbose_name_plural = 'статусы'
    #
    # def __str__(self):
    #     return str('номер: {}, дата: {}, статус: {}'.format(self.room, self.date, self._get_status()))
