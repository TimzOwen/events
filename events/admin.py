from django.contrib import admin
from .models import MyClubUsers
from .models import Event
from .models import Venue

admin.site.register(MyClubUsers)
admin.site.register(Event)


# admin.site.register(Venue)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'zip_code', 'phone', 'web,''email_address')
    ordering = ('name',)
    search_fields = ('name', 'address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name','manager','event_date')
    ordering = ('name',)
    search_fields = ('name','manager')

@admin.register(MyClubUsers)
class MyClubAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')
    ordering = ('first_name',)
    search_fields = ('first_name',)
