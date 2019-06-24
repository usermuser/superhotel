from django.db import models


class Room(models.Model):
    name = models.CharField(verbose_name='имя', max_length=55, unique=True)
    imgage1 = models.ImageField(upload_to='rooms_img/%Y/%m/%d', blank=True)
    imgage2 = models.ImageField(upload_to='rooms_img/%Y/%m/%d', blank=True)
    description = models.TextField(verbose_name='описание номера', blank=True)

    class Meta:
        verbose_name = 'номер'
        verbose_name_plural = 'номера'

    def __str__(self):
        return self.name


class DateItem(models.Model):
    date_item = models.DateField('дата бронирования')
    room = models.ForeignKey('room', on_delete=models.CASCADE,)
    is_busy = models.BooleanField(verbose_name='занят', default=False)

    class Meta:
        verbose_name = 'дата бронирования'
        verbose_name_plural = 'даты бронирования'

    def __str__(self):
        return str(self.date_item)