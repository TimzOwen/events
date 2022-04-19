from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls'))

]

# configure Admin Titles
admin.site.site_header = "Club Admins Page"
admin.site.site_title = "Events "
admin.site.index_title="Manage The events "