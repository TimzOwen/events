from django.db import models


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=120)
    zip_code = models.CharField('Zip Code', max_length=120)
    phone = models.CharField('Contact Phone', max_length=120)
    web = models.URLField('Website Address')
    email_address = models.EmailField('Email address')

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
    # connect two tables
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    # Null and Blank incase no table exits (Foreign connects
    # 1->Many tables
    # venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUsers, blank=True)  # manyToMany connects several events

    def __str__(self):
        return self.name
