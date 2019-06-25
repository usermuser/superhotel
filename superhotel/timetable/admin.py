from django.contrib import admin
from .models import Room, DateItem

class DateItemAdmin(admin.ModelAdmin):
    list_display = ('room','date_item', 'is_busy')
    list_display_links = ('is_busy',)

    def room(self, obj):
        return self.room.name

admin.site.register(Room)
admin.site.register(DateItem, DateItemAdmin)


