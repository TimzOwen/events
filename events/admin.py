from django.contrib import admin
from .models import MyClubUsers
from .models import Event
from .models import Venue


admin.site.register(MyClubUsers)
admin.site.register(Event)
admin.site.register(Venue)

