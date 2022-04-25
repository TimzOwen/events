from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=120)
    zip_code = models.CharField('Zip Code', max_length=120)
    phone = models.CharField('Contact Phone', max_length=120, blank=True)
    web = models.URLField('Website Address', blank=True)
    email_address = models.EmailField('Email address', blank=True)
    owner = models.IntegerField("venue owner",blank=False,default=1)

    def __str__(self):
        return self.name


class MyClubUsers(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=255)
    event_date = models.DateTimeField('Event date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUsers, blank=True)  # manyToMany connects several events

    def __str__(self):
        return self.name
