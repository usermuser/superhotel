from django.contrib import admin
from .models import Room, DateItem, Status

# class DateItemAdmin(admin.ModelAdmin):
#     list_display = ('room','date_item', 'is_busy')
#     list_display_links = ('is_busy',)
#
#     def room(self, obj):
#         return self.room.name

# class DateItemAdmin(admin.ModelAdmin):
#     list_display = ('room','date_item', 'is_busy')
#     list_display_links = ('is_busy',)
#
#     def room(self, obj):
#         return self.status.room
#
#     def is_busy(self, obj):
#         return self.status.is_busy

# class Status(admin.ModelAdmin):
#     list_display = ('is_busy', 'room', 'date')

admin.site.register(Room)
# admin.site.register(DateItem, DateItemAdmin)
admin.site.register(DateItem)
admin.site.register(Status)


