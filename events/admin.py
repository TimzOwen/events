from django.contrib import admin
from .models import MyClubUsers
from .models import Event
from .models import Venue


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'zip_code', 'phone', 'web')
    ordering = ('name',)
    search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name','venue'), 'event_date','description','manager')
    list_display = ('name', 'event_date','venue')
    ordering = ('-event_date',)
    search_fields = ('name', 'manager',)
    list_filter = ('event_date','venue')


@admin.register(MyClubUsers)
class MyClubAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    ordering = ('first_name',)
    search_fields = ('first_name',)
