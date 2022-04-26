from django import forms
from django.forms import ModelForm
from .models import Venue, Event, Speakers


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description')
        labels = {
            'name': '',
            'event_date': 'YYY-MM-DD HH:MM:SS:',
            'venue': 'Venue',
            'manager': 'Manager',
            'attendees': 'Attendees',
            'description': 'Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Date'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Event Venue'}),
            'manager': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Event Manager'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Event attendees'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event description'}),
        }


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Venue'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Zip Code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organizer Phone number'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Web URL Event'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email to event'}),
        }


class SpeakerForm(ModelForm):
    class Meta:
        model = Speakers
        fields = ('speaker_name', 'speaker_role', 'speaker_topic', 'speaker_email', 'speaker_contact')
        labels = {
            'name',
            'role',
            'topic',
            'email',
            'contact'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Speaker Name'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'speaker Role'}),
            'topic': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Topic'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact'})

        }
